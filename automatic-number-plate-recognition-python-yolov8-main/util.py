import string
import easyocr
import re
mo = re.compile(r'[A-Z0-9]')
ticks = re.compile(r'[^a-zA-Z0-9]')


# Initialize the OCR reader
reader = easyocr.Reader(['en'], gpu=False)

# Mapping dictionaries for character conversion
dict_char_to_int = {'O': '0',
                    'I': '1',
                    'J': '3',
                    'A': '4',
                    'G': '6',
                    'S': '5'}

dict_int_to_char = {'0': 'O',
                    '1': 'I',
                    '3': 'J',
                    '4': 'A',
                    '6': 'G',
                    '5': 'S'}


def license_complies_format(text):
    """
    Check if the license plate text complies with the required format.

    Args:
        text (str): License plate text.

    Returns:
        bool: True if the license plate complies with the format, False otherwise.
    """
    new_text = ""
    for char in text:
        if char in mo.findall(text):
            new_text += char


    # if len(new_text) > 8:
    #     return False
    if (new_text[0] in string.ascii_uppercase or new_text[0] in dict_char_to_int.keys()) and \
       (new_text[1] in string.ascii_uppercase or new_text[1] in dict_char_to_int.keys()) and \
       (new_text[2] in string.ascii_uppercase or new_text[2] in dict_char_to_int.keys()) and \
       (new_text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or new_text[3] in dict_int_to_char.keys()) and \
       (new_text[4] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or new_text[4] in dict_int_to_char.keys()) and \
       (new_text[5] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or new_text[5] in dict_int_to_char.keys()) and \
       (new_text[6] in string.ascii_uppercase or new_text[6] in dict_char_to_int.keys()) and \
       (new_text[7] in string.ascii_uppercase or new_text[7] in dict_char_to_int.keys()):

        return True
    else:
        return new_text

def format_license(text):
    """
    Format the license plate text by converting characters using the mapping dictionaries.

    Args:
        text (str): License plate text.

    Returns:
        str: Formatted license plate text.
    """
    license_plate_ = ''
    mapping = {0: dict_int_to_char, 1: dict_int_to_char, 4: dict_char_to_int, 5: dict_char_to_int, 6: dict_int_to_char, 7: dict_int_to_char,
               2: dict_int_to_char, 3: dict_char_to_int}
    for j in [0, 1, 2, 3, 4, 5, 6, 7]:
        if text[j] in mapping[j].keys():
            license_plate_ += mapping[j][text[j]]
        else:
            license_plate_ += text[j]

    return license_plate_

def read_license_plate(license_plate_crop):
    """
    Read the license plate text from the given cropped image.

    Args:
        license_plate_crop (PIL.Image.Image): Cropped image containing the license plate.

    Returns:
        tuple: Tuple containing the formatted license plate text and its confidence score.
    """
    detections = reader.readtext(license_plate_crop)
    #detections = pytesseract.image_to_string(license_plate_crop, config="--psm 8")
    for detection in detections:
        bbox, text, score = detection
        #text = detection
        text = text.upper().replace(' ', '')
        # if license_complies_format(text):

        return text,score
        # if text:
        #     return text, score

    return None, None


def get_car(license_plate, vehicle_track_ids):
    """
    Retrieve the vehicle coordinates and ID based on the license plate coordinates.

    Args:
        license_plate (tuple): Tuple containing the coordinates of the license plate (x1, y1, x2, y2, score, class_id).
        vehicle_track_ids (list): List of vehicle track IDs and their corresponding coordinates.

    Returns:
        tuple: Tuple containing the vehicle coordinates (x1, y1, x2, y2) and ID.
    """
    x1, y1, x2, y2, score, class_id = license_plate

    foundIt = False
    for j in range(len(vehicle_track_ids)):
        xcar1, ycar1, xcar2, ycar2, car_id = vehicle_track_ids[j]

        if x1 > xcar1 and y1 > ycar1 and x2 < xcar2 and y2 < ycar2:
            car_indx = j
            foundIt = True
            break

    if foundIt:
        return vehicle_track_ids[car_indx]

    return -1, -1, -1, -1, -1




