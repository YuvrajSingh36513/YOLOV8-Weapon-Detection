from ultralytics import YOLO
model = YOLO("C:/path to/best.pt")
results = model(source=0, show=True, conf=0.5, save=True)
