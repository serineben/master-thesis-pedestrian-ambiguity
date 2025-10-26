import os
import json
import requests
import base64
from tqdm import tqdm
from PIL import Image
import time

# Configuration
FRAMES_DIR = "/home/serine/datos/newdataset/Frames-extracted/week30"
OUTPUT_DIR = "/home/serine/datos/newdataset/LLAVA-RESULTS/week30_nv"
os.makedirs(OUTPUT_DIR, exist_ok=True)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llava:latest"
TIMEOUT = 60  # Increased timeout for complex scenes
MAX_RETRIES = 3

def analyze_image(image_path):
    """Enhanced pedestrian detection with urban scene understanding"""
    try:
        # First verify the image is valid
        with Image.open(image_path) as img:
            img.verify()
        
        with open(image_path, "rb") as img_file:
            b64_image = base64.b64encode(img_file.read()).decode("utf-8")

        prompt = """Analyze this urban scene carefully and count all visible pedestrians.
        Provide detailed information about each detected person and rejected objects.

        INSTRUCTIONS:
        1. Count ALL pedestrians (walking, standing, partially visible)
        2. Pay special attention to:
           - People near vehicles
           - People in crosswalks
           - People in shadows or behind glass
           - People at different distances
        3. Reject ONLY:
           - Mannequins/statues
           - Posters with human images
           - Reflections
           - Vehicle parts that resemble humans

        RESPONSE FORMAT (JSON):
        {
            "human_count": integer,
            "confidence": 0-1,
            "pedestrians": [
                {
                    "description": "string (e.g., 'adult walking left')",
                    "approximate_age": "child/adult/senior",
                    "position": "left/center/right",
                    "activity": "walking/standing/waiting/etc",
                    "visibility": "clear/partial/occluded"
                }
            ],
            "rejected_items": [
                {
                    "type": "string",
                    "reason": "string",
                    "confidence": 0-1
                }
            ],
            "scene_understanding": "brief_description"
        }"""

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "images": [b64_image],
                "format": "json",
                "stream": False,
                "options": {
                    "temperature": 0.3,  # Balanced creativity/factuality
                    "num_ctx": 4096      # Larger context window
                }
            },
            timeout=TIMEOUT
        )
        
        result = json.loads(response.json().get("response", "{}"))
        
        # Validate and clean the response
        if not isinstance(result, dict):
            raise ValueError("Invalid response format")
            
        # Ensure human_count exists and is numeric
        result["human_count"] = int(result.get("human_count", 0))
        
        # Ensure confidence is within bounds
        result["confidence"] = max(0.0, min(1.0, float(result.get("confidence", 0.0))))
        
        return result
        
    except Exception as e:
        return {
            "human_count": 0,
            "confidence": 0.0,
            "error": str(e),
            "pedestrians": [],
            "rejected_items": []
        }

# Process frames with enhanced error handling
for frame in tqdm(sorted(os.listdir(FRAMES_DIR))):
    if not frame.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue
        
    frame_path = os.path.join(FRAMES_DIR, frame)
    output_path = os.path.join(OUTPUT_DIR, f"{os.path.splitext(frame)[0]}.json")
    
    # Try up to MAX_RETRIES times
    for attempt in range(MAX_RETRIES):
        try:
            result = analyze_image(frame_path)
            with open(output_path, "w") as f:
                json.dump(result, f, indent=2)
            break
        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                error_result = {
                    "human_count": 0,
                    "confidence": 0.0,
                    "error": f"Failed after {MAX_RETRIES} attempts: {str(e)}",
                    "pedestrians": [],
                    "rejected_items": []
                }
                with open(output_path, "w") as f:
                    json.dump(error_result, f, indent=2)
            time.sleep(2)  # Wait before retrying




    for frame_name in tqdm(frames):
        frame_path = os.path.join(frames_dir, frame_name)
        result_path = os.path.join(results_dir, f"{os.path.splitext(frame_name)[0]}.json")
        
        frame = cv2.imread(frame_path)
        height, width = frame.shape[:2]
        
        if os.path.exists(result_path):
            with open(result_path, 'r') as f:
                result = json.load(f)
            
            # Display human count and confidence
            count_text = f"Humans: {result.get('human_count', 0)} (Confidence: {result.get('confidence', 0):.2f})"
            cv2.putText(frame, count_text, (20, 40), font, font_scale, text_color, font_thickness)
            
            # Draw approximate boxes based on position descriptions
            for i, pedestrian in enumerate(result.get('pedestrians', [])):
                # Create approximate box based on position description
                if 'position' in pedestrian:
                    if pedestrian['position'] == 'left':
                        x1, x2 = 0, width//3
                    elif pedestrian['position'] == 'right':
                        x1, x2 = 2*width//3, width
                    else:  # center
                        x1, x2 = width//3, 2*width//3
                    
                    # Vertical position is arbitrary since we don't have that data
                    y1, y2 = height//2, height
                    
                    # Draw box
                    cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 2)
                    
                    # Add description
                    desc = f"{pedestrian.get('approximate_age', 'person')} {pedestrian.get('activity', '')}"
                    cv2.putText(frame, desc, (x1, y1-10), font, font_scale*0.6, text_color, 1)
        






























