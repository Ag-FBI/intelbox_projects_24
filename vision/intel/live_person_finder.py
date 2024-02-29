from pathlib import Path
import pickle
import numpy as np
import face_recognition, imutils
from datetime import datetime
from collections import Counter
import cv2
import PySimpleGUI as sg
from multiprocessing import Lock, Queue


DEFAULT_ENCODINGS_PATH = Path("../output/encodings.pkl")
def recognize_faces(
   # image_location: np.ndarray,
    model: str = "hog",
    encodings_location: Path = DEFAULT_ENCODINGS_PATH,
) -> None:
    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)

    #input_image = face_recognition.load_image_file(image_location)
    input_image = face_recognition.load_image_file(Path("../pictures/Miss Fred/Freddie2.jpg"))
    input_face_locations = face_recognition.face_locations(
        input_image, model=model
    )
    input_face_encodings = face_recognition.face_encodings(
        input_image, input_face_locations
    )

    for bounding_box, unknown_encoding in zip(
        input_face_locations, input_face_encodings
    ):
        name = _recognize_face(unknown_encoding, loaded_encodings)
        if not name:
            name = "Unknown"
        print(name)
        #print(name, bounding_box)

def _recognize_face(unknown_encoding, loaded_encodings):
    boolean_matches = face_recognition.compare_faces(
        loaded_encodings["encodings"], unknown_encoding
    )
    votes = Counter(
        name
        for match, name in zip(boolean_matches, loaded_encodings["names"])
        if match
    )
    if votes:
        return votes.most_common(1)[0][0]
    
# def findFaceInFrame(input_frames, output_frames):
#     try:
#         frame = input_frames.get_nowait()
        
#     except:
#         print('queue is empty')
#         #return True
#     else:
#         face_cascade = cv2.CascadeClassifier('classifiers/faceclassifier.xml')
#         detected_name = recognize_faces(frame)
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
#         faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#             # Draw the rectangle around each face
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#             cv2.putText(frame, detected_name, (x, y - 5),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,100), 2)
#         processedgray = cv2.imencode('.png', frame)[1].tobytes()
#         output_frames.put(processedgray)
#     return

# def live_person_finder():
#     input_frames = Queue()
#     output_frames = Queue()
#     # define the window layout
#     layout = [[sg.Text('Live Person Finder')],
#               [sg.Image(filename='', key='liveimage'),  sg.Image(filename='', key='processedimage')],
#               [sg.Column([[sg.Button('Start', size=(10, 1), font='Helvetica 14'),
#                sg.Button('Capture', size=(10, 1), font='Any 14'),
#                sg.Button('Stop', size=(10, 1), font='Any 14'),
#                sg.Button('Exit', size=(10, 1), font='Helvetica 14'), ]], justification='center')],
#               ]

#     # create the window and show it without the plot
#     window = sg.Window('IntelEagle',
#                        layout, keep_on_top=True, no_titlebar=False, modal=True, transparent_color=sg.theme_background_color(), resizable=True)

#     # ---===--- Event LOOP Read and display frames, operate the GUI --- #
#     cap = cv2.VideoCapture(0)
#     recording = False
#     while True:
#         event, values = window.read(timeout=20)
#         if event == 'Exit' or event == sg.WIN_CLOSED:
#             cap.release()
#             window.close()
#             break

#         elif event == 'Start':
#             recording = True

#         elif event == 'Stop':
#             recording = False
#             img = np.full((20, 20), 0)
#             # this is faster, shorter and needs less includes
#             imgbytes = cv2.imencode('.png', img)[1].tobytes()
#             window['liveimage'].update(data=imgbytes)
#             window['processedimage'].update(data=imgbytes)

#         if recording:
#             ret, frame = cap.read()
#             frame = imutils.resize(frame, width=320)
#             imgbytes = cv2.imencode('.png', frame)[1].tobytes()  # ditto

#             if event == 'Capture':
#                 now = datetime.now()
#                 current_time = now.strftime("%y%m%d%H:%M:%S")
#                 filename = current_time+".png"
#                 cv2.imwrite(filename, frame)


#             input_frames.put(frame)
#             window['liveimage'].update(data=imgbytes)
#             findFaceInFrame(input_frames, output_frames)
#             window['processedimage'].update(data=output_frames.get())
        
#     window.close()

recognize_faces()