import cv2
import mysql.connector
from tkinter import messagebox
import requests
import base64
import numpy as np

class UserAuthentication:
    def __init__(self, face_classifier_path, license_plate_classifier_path, database_config, api_url):
        # Load face and license plate classifiers
        self.face_cascade = cv2.CascadeClassifier(face_classifier_path)
        self.license_plate_cascade = cv2.CascadeClassifier(license_plate_classifier_path)
        

        # Connect to MySQL database
        self.db = mysql.connector.connect(**database_config)
        self.cursor = self.db.cursor()

        # API endpoint for image uploads
        self.api_url = api_url
        
    def process_image_from_django(self, image_data):
        # Decode base64 image data
        decoded_image = base64.b64decode(image_data)
        np_array = np.frombuffer(decoded_image, np.uint8)
        img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

        # Perform face and license plate detection
        faces = self.face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        license_plates = self.license_plate_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Process and send feedback based on the detection results
        if len(faces) == 1 or len(license_plates) == 1:
            # Match found in the database
            messagebox.showinfo("Match Found", "User authenticated successfully!")
        else:
            # No match found
            messagebox.showinfo("No Match Found", "User not found in the database.")

    def upload_image_to_django(self, image_data):
        # Example API call to upload image data to Django web app
        payload = {'image_data': image_data}
        response = requests.post(self.api_url + '/upload/', json=payload)

        if response.status_code == 200:
            self.process_image_from_django(response.json().get('image_data'))
        else:
            # Handle API upload failure
            messagebox.showerror("API Upload Error", "Failed to upload image to Django.")



