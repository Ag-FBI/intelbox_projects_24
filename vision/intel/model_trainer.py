from pathlib import Path

import face_recognition
import pickle
from collections import Counter

DEFAULT_ENCODINGS_PATH = Path("..\output\encodings.pkl")

Path("..\pictures").mkdir(exist_ok=True)
Path("..\output").mkdir(exist_ok=True)


def encode_known_faces(
    model: str = "hog", encodings_location: Path = DEFAULT_ENCODINGS_PATH
) -> None:
    names = []
    encodings = []

    for filepath in Path("..\pictures").glob("*/*"):
        name = filepath.parent.name
        image = face_recognition.load_image_file(filepath)

        face_locations = face_recognition.face_locations(image, model=model)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        for encoding in face_encodings:
            names.append(name)
            encodings.append(encoding)

    name_encodings = {"names": names, "encodings": encodings}
    with encodings_location.open(mode="wb") as f:
        pickle.dump(name_encodings, f)
    
encode_known_faces()

# def _recognize_face(unknown_encoding, loaded_encodings):
#     boolean_matches = face_recognition.compare_faces(
#         loaded_encodings["encodings"], unknown_encoding
#     )
#     votes = Counter(
#         name
#         for match, name in zip(boolean_matches, loaded_encodings["names"])
#         if match
#     )
#     if votes:
#         return votes.most_common(1)[0][0]
    
