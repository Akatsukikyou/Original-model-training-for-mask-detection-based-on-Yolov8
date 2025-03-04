from ultralytics import YOLO

# Load a model
#model = YOLO("yolov8n.yaml")  # build a new model from YAML
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
#model = YOLO("./data/yolov8n.yaml").load("yolov8n.pt")  # build from YAML and transfer weights

# Train the model
results =model.train(data="mask.yaml", epochs=10, imgsz=640,workers=0)

results = model.val()