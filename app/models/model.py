from ultralytics import YOLO

def load_model(checkpoint_path: str):
    model = YOLO(checkpoint_path)
    return model

def predict_image(model, image_path):
    return model.predict(image_path)