import tkinter as tk
from PIL import Image, ImageTk
import threading
import time
import admin
import cv2
from transformers import ViTImageProcessor, ViTForImageClassification

# Load the pre-trained ViT model for image classification
model = ViTForImageClassification.from_pretrained('giecom/giecom-vit-model-clasification-waste')

def start_camera_with_delay(root):
    time.sleep(1)

def update_image(root, label_image, label_result, video_capture):
    frame_count = 0
    while True:
        try:
            ret, frame = video_capture.read()
            if not ret:
                break
            
            frame_count += 1
            if frame_count % 10 != 0:  # Skip frames until the 10th frame
                continue
            
            # Convert OpenCV BGR frame to PIL RGB image
            image_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            image_pil.thumbnail((640, 480))
            tk_image = ImageTk.PhotoImage(image_pil)
            label_image.config(image=tk_image)
            label_image.image = tk_image

            processor = ViTImageProcessor.from_pretrained('giecom/giecom-vit-model-clasification-waste')
            inputs = processor(images=image_pil, return_tensors="pt")

            outputs = model(**inputs)
            logits = outputs.logits
            predicted_class_idx = logits.argmax(-1).item()
            predicted_class = model.config.id2label[predicted_class_idx]

            # Update label text with predicted class
            label_result.config(text="Predicted class: " + predicted_class)

        except Exception as e:
            print(f"Error: {e}")
            break
    
    # Release video capture object
    video_capture.release()

    # Call on_closing to close the window after video finished
    root.after(100, lambda: on_closing(root))

def on_closing(root):
    root.destroy()

def start_tkinter():
    # Create Tkinter window
    root = tk.Tk()
    root.title("Image Classification")
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))

    # Display initial image in Tkinter window
    label_image = tk.Label(root)
    label_image.pack()

    # Label to display the result
    label_result = tk.Label(root, text="")
    label_result.pack()

    # Open the video file
    video_capture = cv2.VideoCapture('../data/video/test_video.mp4')

    # Update the image and perform classification using frames from the video
    update_thread = threading.Thread(target=update_image, args=(root, label_image, label_result, video_capture))
    update_thread.start()

    # Button to open admin panel
    admin_button = tk.Button(root, text="Admin Panel", command=lambda: admin.open_admin_page(root))
    admin_button.pack()

    # Start Tkinter event loop
    root.mainloop()

# Call the function to start the Tkinter app
start_tkinter()
