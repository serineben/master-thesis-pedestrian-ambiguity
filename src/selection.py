import os
import cv2
import shutil
from tkinter import *
from PIL import Image, ImageTk

# Configuration
frames_dir = "frames_extracted_part1"  # Folder containing all extracted frames
selected_dir = "frames_extracted_part1/part2"  # Folder for selected frames

# Create the destination folder if it doesn't exist
os.makedirs(selected_dir, exist_ok=True)

# Get all image files in the source folder
image_files = [f for f in os.listdir(frames_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
image_files.sort()  # Sort files by name

# Initialize GUI
root = Tk()
root.title("Image Selection with People")
root.geometry("1200x800")

# Global variables
current_index = 0
selected_images = []

# Function to display the current image
def show_current_image():
    global current_index, img_label, file_label, progress_label

    if 0 <= current_index < len(image_files):
        # Load the image
        img_path = os.path.join(frames_dir, image_files[current_index])
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Resize for display if necessary
        height, width = img.shape[:2]
        max_height = 600
        if height > max_height:
            scale = max_height / height
            img = cv2.resize(img, (int(width * scale), max_height))

        # Convert for Tkinter
        img_tk = ImageTk.PhotoImage(image=Image.fromarray(img))
        img_label.config(image=img_tk)
        img_label.image = img_tk

        # Update labels
        file_label.config(text=f"File: {image_files[current_index]}")
        progress_label.config(text=f"Image {current_index + 1}/{len(image_files)} | Selected: {len(selected_images)}")

# Function to go to the next image
def next_image():
    global current_index
    if current_index < len(image_files) - 1:
        current_index += 1
        show_current_image()

# Function to go to the previous image
def prev_image():
    global current_index
    if current_index > 0:
        current_index -= 1
        show_current_image()

# Function to select the current image
def select_image():
    global current_index, selected_images

    if 0 <= current_index < len(image_files):
        img_name = image_files[current_index]
        if img_name not in selected_images:
            selected_images.append(img_name)

            # Copy the image to the destination folder
            src_path = os.path.join(frames_dir, img_name)
            dst_path = os.path.join(selected_dir, img_name)
            shutil.copy2(src_path, dst_path)

            # Update progress label
            progress_label.config(text=f"Image {current_index + 1}/{len(image_files)} | Selected: {len(selected_images)}")

            # Automatically go to the next image
            next_image()

# Create widgets
frame = Frame(root)
frame.pack(pady=20)

# Label to display the image
img_label = Label(frame)
img_label.pack()

# Info labels
file_label = Label(root, text="")
file_label.pack(pady=5)

progress_label = Label(root, text="")
progress_label.pack(pady=5)

# Navigation and selection buttons
button_frame = Frame(root)
button_frame.pack(pady=10)

prev_button = Button(button_frame, text="Previous", command=prev_image, width=15, height=2)
prev_button.grid(row=0, column=0, padx=10)

select_button = Button(button_frame, text="Select", command=select_image, width=15, height=2, bg="green", fg="white")
select_button.grid(row=0, column=1, padx=10)

next_button = Button(button_frame, text="Next", command=next_image, width=15, height=2)
next_button.grid(row=0, column=2, padx=10)

# Keyboard shortcuts
root.bind("<Left>", lambda event: prev_image())
root.bind("<Right>", lambda event: next_image())
root.bind("<space>", lambda event: select_image())

# Show the first image
show_current_image()

# Start the application
root.mainloop()

print(f"Selection completed. {len(selected_images)} images have been copied to the folder '{selected_dir}'.")
