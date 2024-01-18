import cv2
import mysql.connector
from tkinter import messagebox
from Notification import NotificationSystem
from UserAuth import UserAuthentication
from GUI import MyApp
import tkinter as tk



if __name__ == "__main__":
    root = tk.Tk()
    
    notification_system = NotificationSystem(root)
    app = MyApp(root, notification_system)
    root.mainloop()

# Connecting to the Database
    face_classifier_path = "faceclassifier.xml"
    license_plate_classifier_path = "haarclassifier.xml"
    database_config = {
        'host': 'localhost',
        'user': 'shedrack',
        'password': 'shedrack.1995',
        'database': 'computer_vision'
    }
    
    try:
        connection = mysql.connector.connect(**database_config)
        print("Connected to the database.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
# Example of triggering a notification
        notification_message = f"Notification: Hello, {entered_name}!"
        self.notification_system.show_notification(notification_message)

'''api_url = 'http://your-django-app-api-url'


user_authenticator = UserAuthentication(face_classifier_path, license_plate_classifier_path, database_config)

user_authenticator.authenticate_user("path/to/image.jpg")
# Example usage: upload image data to Django
image_data = 'base64_encoded_image_data'
user_auth.upload_image_to_django(image_data)'''





    
