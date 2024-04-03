import tkinter as tk
from PIL import Image, ImageTk
import threading
import camera
import time
import admin
from transformers import ViTImageProcessor, ViTForImageClassification

# Load the pre-trained ViT model for image classification
model = ViTForImageClassification.from_pretrained('giecom/giecom-vit-model-clasification-waste')

def start_camera_with_delay(root):
    time.sleep(1)  
    camera.save_frame_camera_cycle(0, '../data/temp', '1', 20)

def update_image(root, label_image, label_result):
    image_path = '../data/temp/1_default.jpg'
    
    while True:
        try:
            image_pil = Image.open(image_path)
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

            break  # Exit the loop if image opening and classification were successful
            
        except (FileNotFoundError, OSError) as e:
            # If the file is not found or cannot be opened, log the error and retry after a delay
            print(f"Error opening image file: {e}")
            time.sleep(1)  # Wait for 1 second before retrying
        except Exception as e:
            # Catch any other exceptions that might occur when opening the image
            print(f"Error: {e}")
            break  # Exit the loop if an unexpected error occurs
    
    # Call update_image again after 100 milliseconds
    if not exit_flag:
        root.after(100, update_image, root, label_image, label_result)


def on_closing(root):
    global exit_flag
    exit_flag = True
    root.destroy()
    camera.release_camera()

def start_tkinter():
    global exit_flag
    exit_flag = False
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

    # Start camera function in a separate thread with a delay
    camera_thread = threading.Thread(target=start_camera_with_delay, args=(root,))
    camera_thread.start()

    # Update the image and perform classification periodically
    update_image(root, label_image, label_result)

    # Button to open admin page
    admin_button = tk.Button(root, text="Admin Page", command=lambda: admin.open_admin_page(root))
    admin_button.pack()

    # Start Tkinter event loop
    root.mainloop()

# Call the function to start the Tkinter app
start_tkinter()

