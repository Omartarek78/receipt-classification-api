from fastapi import FastAPI
from app.routes import predict
from fastapi.responses import JSONResponse
app = FastAPI()

@app.get("/health")
def health_check():
    return JSONResponse(content={"message": "API is up and running"})

app.include_router(predict.router)
