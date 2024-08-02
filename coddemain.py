
import os
import cv2
import numpy as np
import shutil

def is_blank_or_humanless(image_path):
    """Checks if an image is blank, lacks humans, or lacks faces."""
    try:
        image = cv2.imread(image_path)
        if np.all(image == 0):
            return True

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if np.mean(gray) < 10: 
            return True
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  
        faces = face_cascade.detectMultiScale(image, 1.3, 5)

        if len(faces) == 0:
            return True

        net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'mobilenet_iter_73000.caffemodel')

        return False

    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return False
 
def move_images(source_folder, destination_folder, destination_folder1):
    """Moves images based on their characteristics."""
    os.makedirs(destination_folder, exist_ok=True)
    os.makedirs(destination_folder1, exist_ok=True)
 
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            image_path = os.path.join(source_folder, filename)
 
            if is_blank_or_humanless(image_path):
                shutil.copy(image_path, destination_folder)
                print(f"Moved {filename} to {destination_folder}")
            else:
                shutil.copy(image_path, destination_folder1)
                print(f"Moved {filename} to {destination_folder1}")
 
if __name__ == "__main__":
    source_folder = r"C:\\Users\\398504\\CRF\\crf23\\Gold_photo_verification_122016\\downloaded_images\\"
    destination_folder = r"C:\\Users\\398504\\CRF\\crf23\\Gold_photo_verification_122016\\fake\\"
    destination_folder1 = r"C:\\Users\\398504\\CRF\\crf23\\Gold_photo_verification_122016\\real\\"
 
    move_images(source_folder, destination_folder, destination_folder1)