import cv2
from ultralytics import YOLO
import imutils
import json
import requests

recipient = "url_path"
video_address = "live_feed"

coco_model = YOLO('yolov8n.pt')
license_plate_detector = YOLO('license_plate_detector.pt')

file = 'json_file'


cap = cv2.VideoCapture(video_address)

from sort import *
from util import get_car, read_license_plate, write_csv


results = {}
data = {}

mot_tracker = Sort()

vehicles = [2, 3, 5, 7]

# read frames
text = -1
bbox = -1
frame_nmr = -1
ret = True
while ret:
    frame_nmr += 1
    text +=1
    bbox +=1
    ret, frame = cap.read()
    if ret:
        if frame_nmr > 30:
            break
        results[frame_nmr] = {}
        data["text"] = {}
        data["bbox"] = {}

        # detect vehicles
        detections = coco_model(frame)[0]
        detections_ = []
        for detection in detections.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detection
            if int(class_id) in vehicles:
                detections_.append([x1, y1, x2, y2, score])

        # track vehicles
        try:
            track_ids = mot_tracker.update(np.asarray(detections_))
        except Exception as e:
            pass

        # detect license plates
        license_plates = license_plate_detector(frame)[0]
        for license_plate in license_plates.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = license_plate

            # assign license plate to car
            xcar1, ycar1, xcar2, ycar2, car_id = get_car(license_plate, track_ids)

            if car_id != -1:

                # crop license plate
                license_plate_crop = frame[int(y1):int(y2), int(x1): int(x2), :]
                license_plate_crop = cv2.rotate(license_plate_crop, cv2.ROTATE_180)
                h, w = license_plate_crop.shape[:2]
                new_height = int(0.8 * h)
                end_row, end_col = new_height, w

                cropped_image = license_plate_crop[0:end_row, 0:end_col]

                # process license plate
                license_plate_crop_gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
                license_plate_edged = cv2.Canny(license_plate_crop_gray, 30, 200)
                cnts, new = cv2.findContours(license_plate_edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                #_, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 167, 255, cv2.THRESH_BINARY_INV)
                license_plate_crop_thresh = cv2.adaptiveThreshold(license_plate_crop_gray, 255,
                                                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,
                                                                 11, 2)
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
                adaptive_thresh = cv2.morphologyEx(license_plate_crop_thresh, cv2.MORPH_CLOSE, kernel)
                contours = cv2.findContours(adaptive_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(contours)
                sorted_cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:15]
                rotated = cv2.rotate(license_plate_crop_thresh, cv2.ROTATE_180)

                for contour in sorted_cnts:
                    cv2.drawContours(cropped_image, [contour], -1, (0,255,0), 2)




                #read license plate
                license_plate_text, confidence_score = read_license_plate(rotated)

                if license_plate_text is not None:
                    results[frame_nmr][car_id] = {"car":{"bbox":[ xcar1, ycar1, xcar2, ycar2]},
                                                  "license_plate":{"bbox":[x1, y1, x2, y2],
                                                  "text": license_plate_text,
                                                  "bbox_score":score,
                                                   "text_score":confidence_score
                                                    }}
                    for frame_nmr, details in results.items():
                        for car_id, items in details.items():
                            data = {"text":f"{items['license_plate']['text']}",
                            "bbox":f"{items['license_plate']['bbox']}"}
                            requests.post(recipient, data)
