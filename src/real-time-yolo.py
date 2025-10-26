from ultralytics import YOLO
import cv2

# Load YOLOv8m model (replace with your custom model if needed)
model = YOLO("yolov8m.pt")  # Official COCO-pretrained model (detects 'person' class)

# Open video capture (choose one)
cap = cv2.VideoCapture("/home/serine/datos/properdata/GX010212.MP4")          # Webcam (device 0)
# cap = cv2.VideoCapture("video.mp4")  # Video file
# cap = cv2.VideoCapture("rtsp://...") # IP camera (RTSP stream)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 inference
    results = model(frame, classes=[0])  # Only detect 'person' (class 0 in COCO)

    # Visualize results
    annotated_frame = results[0].plot()  # Draw bounding boxes + labels

    # Display the annotated frame
    cv2.imshow("YOLOv8 Real-Time Pedestrian Detection", annotated_frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()