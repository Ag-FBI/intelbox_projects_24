# Computer Vision Security System
# Overview
The Computer Vision Security System is a comprehensive project that integrates a Python Desktop App with computer vision capabilities for live facial recognition and license plate identification, using OpenCV and a Python Haar classifier. Additionally, a Django web application serves as the user interface for the vision engine. This system allows users, both military and civilian, to upload images of individuals or license plates of interest, triggering the desktop application to process the data and provide feedback.
The feedback includes pertinent details such as Name, date posted, vehicle type, color, owner, and time captured. All this information is stored in a MySQL database table, which is linked to both the desktop application and the web application. The front-end framework for the web application is Bootstrap, ensuring a responsive and user-friendly interface.

## Key Features

 **Facial Recognition:** Utilizes computer vision capabilities for live facial recognition.
 **License Plate Identification:** Implements a Python Haar classifier for license plate identification.
 **Desktop App:** Processes live video feeds and provides real-time feedback.
 **Web Application:** Allows users to upload images and access the vision engine through a user-friendly interface.
 **MySQL Database:** Stores feedback details, creating a centralized repository.
 **Security Measures:** Implements secure communication protocols, user authentication, and authorization mechanisms.
 **Civilian Data Contribution:** Civilian users can upload information, and the military receives notifications only on a positive match.

## Getting Started

### Prerequisites

- Python (3.7 and above)
- Django
- OpenCV
- MySQL Database

**Setup the MySQL Database:**
Install MySQL Server:

Ensure that MySQL Server is installed on your machine. If not, download and install it from the official MySQL website.

Create a Database:

Open a MySQL command line or a MySQL client of your choice and create a new database for the Computer Vision Security System:


CREATE DATABASE computer_vision_db;
You can replace computer_vision_db with your preferred database name.

Create a Database User:
Create a dedicated user for the Computer Vision Security System with the necessary privileges:

CREATE USER 'cv_user'@'localhost' IDENTIFIED BY 'your_password';
Replace 'cv_user' with your desired username and set a strong password for 'your_password'.

Grant Permissions:

Grant the required permissions to the newly created user for the database:


GRANT ALL PRIVILEGES ON computer_vision_db.* TO 'cv_user'@'localhost';
Flush privileges to apply the changes:


FLUSH PRIVILEGES;
Database Configuration in Django:

Open the settings.py file in the Django project (/path/to/your/project/settings.py) and update the database configuration section:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        **'NAME': 'computer_vision_db',**
        'USER': 'cv_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Make sure to replace 'cv_user' and 'your_password' with the credentials you set earlier.

Run Migrations:

Apply the initial migrations to create the necessary tables in the database:


python manage.py migrate
This command will create the required tables based on the Django models.

#We welcome contributions! If you'd like to contribute to the project, please follow our Contribution Guidelines.




### Installation

1. Clone the repository:
 ```bash
   git clone https://github.com/Ag-FBI/intelbox_projects_24.git
