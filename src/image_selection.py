"""
image_selection.py

GUI tool for manually selecting frames with people from extracted video frames.
Selected frames are copied to a separate folder for further processing.
"""

import os
import cv2
import shutil
from tkinter import *
from PIL import Image, ImageTk

# ---------------------- Configuration ----------------------
FRAMES_DIR = "frames_extracted_part1"          # Folder containing all extracted frames
SELECTED_DIR = "frames_extracted_part1/part2"  # Folder for selected frames
os.makedirs(SELECTED_DIR, exist_ok=True)

# Get sorted list of image files
image_files = sorted([f for f in os.listdir(FRAMES_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

# ---------------------- GUI Setup ----------------------
root = Tk()
root.title("Image Selection with People")
root.geometry("1200x800")

# Global variables
current_index = 0
selected_images = []

# ---------------------- Functions ----------------------
def show_current_image():
    """Display the current image in the GUI with progress info."""
    global current_index, img_label, file_label, progress_label

    if 0 <= current_index < len(image_files):
        img_path = os.path.join(FRAMES_DIR, image_files[current_index])
        img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)

        # Resize for display if too large
        max_height = 600
        if img.shape[0] > max_height:
            scale = max_height / img.shape[0]
            img = cv2.resize(img, (int(img.shape[1]*scale), max_height))

        img_tk = ImageTk.PhotoImage(Image.fromarray(img))
        img_label.config(image=img_tk)
        img_label.image = img_tk

        file_label.config(text=f"File: {image_files[current_index]}")
        progress_label.config(text=f"Image {current_index + 1}/{len(image_files)} | Selected: {len(selected_images)}")

def next_image():
    """Move to the next image."""
    global current_index
    if current_index < len(image_files) - 1:
        current_index += 1
        show_current_image()

def prev_image():
    """Move to the previous image."""
    global current_index
    if current_index > 0:
        current_index -= 1
        show_current_image()

def select_image():
    """Select the current image and copy it to the selected folder."""
    global current_index, selected_images

    img_name = image_files[current_index]
    if img_name not in selected_images:
        selected_images.append(img_name)
        shutil.copy2(os.path.join(FRAMES_DIR, img_name), os.path.join(SELECTED_DIR, img_name))
        progress_label.config(text=f"Image {current_index + 1}/{len(image_files)} | Selected: {len(selected_images)}")
        next_image()

# ---------------------- Widgets ----------------------
frame = Frame(root)
frame.pack(pady=20)

img_label = Label(frame)
img_label.pack()

file_label = Label(root, text="")
file_label.pack(pady=5)

progress_label = Label(root, text="")
progress_label.pack(pady=5)

button_frame = Frame(r_
