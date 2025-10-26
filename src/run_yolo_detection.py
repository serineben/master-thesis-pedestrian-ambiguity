import os
import cv2
import json
from ultralytics import YOLO
from tqdm import tqdm

# Configuration
FRAMES_DIR = "/home/serine/datos/newdataset/Frames-extracted/week30"
OUTPUT_DIR = "/home/serine/datos/newdataset/YOLO-RESULTS/week30_nv"

# Create output directories
os.makedirs(f"{OUTPUT_DIR}/detected_persons", exist_ok=True)
os.makedirs(f"{OUTPUT_DIR}/ambiguous", exist_ok=True)
os.makedirs(f"{OUTPUT_DIR}/metadata", exist_ok=True)

# Load YOLO model with optimized settings
model = YOLO("yolov8m.pt")
CONF_HIGH = 0.6  # High confidence threshold for clear detections
CONF_LOW = 0.4   # Low confidence threshold for ambiguous cases
MIN_HEIGHT = 80  # Minimum pixel height for valid detection

def draw_boxes(image, detections, color):
    """Draw bounding boxes with confidence labels"""
    annotated = image.copy()
    for det in detections:
        x1, y1, x2, y2 = det["bbox"]
        conf = det["confidence"]
        
        # Draw rectangle
        cv2.rectangle(annotated, (x1, y1), (x2, y2), color, 2)
        
        # Draw label background
        label = f"person: {conf:.2f}"
        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        cv2.rectangle(annotated, (x1, y1 - h - 10), (x1 + w, y1), color, -1)
        
        # Draw label text
        cv2.putText(annotated, label, (x1, y1 - 5), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)
    return annotated

def process_frame(frame_path):
    """Process a single frame with improved detection logic"""
    img = cv2.imread(frame_path)
    if img is None:
        return None
    
    frame_name = os.path.basename(frame_path)
    frame_data = {
        "frame": frame_name,
        "detections": [],
        "human_count": 0,
        "decision": "none",
        "max_confidence": 0.0
    }

    # Run detection with two confidence levels
    results = model(img, conf=CONF_LOW, classes=[0])  # Only detect persons
    
    # Process detections with size filtering
    for r in results:
        for box in r.boxes:
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            height = y2 - y1
            
            # Apply size filter
            if height < MIN_HEIGHT:
                continue
                
            detection = {
                "bbox": [x1, y1, x2, y2],
                "confidence": conf
            }
            frame_data["detections"].append(detection)
            
            if conf > frame_data["max_confidence"]:
                frame_data["max_confidence"] = conf

    # Categorize frame based on detections
    high_conf_detections = [d for d in frame_data["detections"] if d["confidence"] >= CONF_HIGH]
    low_conf_detections = [d for d in frame_data["detections"] if CONF_LOW <= d["confidence"] < CONF_HIGH]
    
    frame_data["human_count"] = len(high_conf_detections)
    
    # Make decision and save visualizations
    if high_conf_detections:
        frame_data["decision"] = "person"
        output_subdir = "detected_persons"
        annotated_img = draw_boxes(img, high_conf_detections, (0, 255, 0))  # Green for high confidence
    elif low_conf_detections:
        frame_data["decision"] = "ambiguous"
        output_subdir = "ambiguous"
        annotated_img = draw_boxes(img, low_conf_detections, (0, 255, 255))  # Yellow for ambiguous
    else:
        return None  # Skip frames with no detections

    # Save visual output
    cv2.imwrite(f"{OUTPUT_DIR}/{output_subdir}/{frame_name}", annotated_img)
    
    # Save metadata
    with open(f"{OUTPUT_DIR}/metadata/{os.path.splitext(frame_name)[0]}.json", "w") as f:
        json.dump(frame_data, f, indent=2)
    
    return frame_data

# Process all frames with progress bar
frame_files = [f for f in os.listdir(FRAMES_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
for frame_file in tqdm(frame_files, desc="Processing frames"):
    process_frame(f"{FRAMES_DIR}/{frame_file}")

print(f"\nProcessing complete. Results saved to: {OUTPUT_DIR}")















































