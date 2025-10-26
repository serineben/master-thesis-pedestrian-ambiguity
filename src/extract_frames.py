"""
extract_frames.py

Extracts frames from a video file using ffmpeg.
Supports configurable frame intervals and provides basic error handling.
Outputs frames as JPG images into a specified folder.
"""

import subprocess
import json
import os

# ---------------------- Configuration ----------------------
VIDEO_PATH = "/home/serine/datos/Week30_2018-10-04/2018-10-04-11-28-13_Dataset_year-A3.h264"
OUTPUT_DIR = "frames_extracted"
FRAME_INTERVAL = 10  # Extract one frame every N frames

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------- Frame Extraction ----------------------
try:
    # Get detailed information about the video file
    cmd = f'ffprobe -v error -show_entries format=duration -show_streams -of json "{VIDEO_PATH}"'
    result = subprocess.check_output(cmd, shell=True)
    info = json.loads(result)
    print("Video file information:")
    print(json.dumps(info, indent=2))
    
    # Extract frames every FRAME_INTERVAL frames
    cmd = f'ffmpeg -i "{VIDEO_PATH}" -vf "select=not(mod(n\\,{FRAME_INTERVAL}))" -vsync vfr "{OUTPUT_DIR}/frame_%04d.jpg"'
    print(f"Extracting one frame every {FRAME_INTERVAL} frames...")
    subprocess.call(cmd, shell=True)
    
    # Verify the number of frames extracted
    frames = [f for f in os.listdir(OUTPUT_DIR) if f.endswith('.jpg')]
    print(f"Number of frames extracted: {len(frames)}")
    
except Exception as e:
    print(f"Error during extraction: {e}")
    
    # Fallback: try a basic extraction if the above fails
    print("Attempting alternative extraction method...")
    cmd = f'ffmpeg -i "{VIDEO_PATH}" "{OUTPUT_DIR}/frame_%04d.jpg"'
    subprocess.call(cmd, shell=True)
    
    # Verify again
    frames = [f for f in os.listdir(OUTPUT_DIR) if f.endswith('.jpg')]
    print(f"Number of frames extracted with alternative method: {len(frames)}")
