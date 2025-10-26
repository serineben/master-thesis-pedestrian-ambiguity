"""
real_time_yolo.py

Real-time pedestrian detection using YOLOv8m.
Supports video files, webcam, or RTSP streams.
Displays annotated frames with bounding boxes and labels.
"""

import cv2
from ultralytics import YOLO

# ---------------------- Configuration ----------------------
MODEL_PATH = "yolov8m.pt"  # Path to YOLOv8 model (replace with custom model if needed)
VIDEO_SOURCE = "/home/serine/datos/properdata/GX010212.MP4"
# Alternative sources:
# VIDEO_SOURCE = 0           # Webcam (device 0)
# VIDEO_SOURCE = "rtsp://..." # IP camera (RTSP stream)

# Load YOLOv8 model
model = YOLO(MODEL_PATH)  # COCO-pretrained model (detects 'person' class)

# Open video capture
cap = cv2.VideoCapture(VIDEO_SOURCE)

# ---------------------- Main Loop ----------------------
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 inference (detect only 'person' class)
    results = model(frame, classes=[0])

    # Visualize results: draw bounding boxes + labels
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLOv8 Real-Time Pedestrian Detection", annotated_frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
