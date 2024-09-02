from fastapi import APIRouter, UploadFile, File
from app.models.model import load_model, predict_image
from fastapi.responses import JSONResponse
from tempfile import NamedTemporaryFile
router = APIRouter()
import os

model = load_model("app/models/checkpoints/best.pt")

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint to handle prediction requests.
    
    Args:
        file (UploadFile): The image file uploaded by the client for prediction.

    Returns:
        JSONResponse: A JSON response containing the prediction class and confidence level 
                      or an error message if something goes wrong.
    """
        
    try:
        with NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(await file.read())
            temp_file_path = temp_file.name


        prediction = predict_image(model,temp_file_path)
        
        os.remove(temp_file_path)

        if  prediction[0].boxes.cls.numel() ==1 and prediction[0].boxes.conf >= 0.8:
            return JSONResponse(content={"prediction": prediction[0].boxes.cls.item()
                                         ,
                                         "confidence level": prediction[0].boxes.conf.item()})
        else:
            return JSONResponse(content={"prediction": -1})


    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
