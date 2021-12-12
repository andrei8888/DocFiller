import os
from pytesseract.pytesseract import Output
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def clear_string(text):
    text = os.linesep.join([s for s in text.splitlines() if s])
    text = " ".join(text.split())
    return text


def get_text(img):
    img = cv2.resize(img, (0, 0), fx=3, fy=3)
    text = pytesseract.image_to_string(img, lang="ron")
    text = clear_string(text)
    return text


def get_informatii(img, inf):
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        text = d['text'][i]
        if text == "ROUMANIE":
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    pattern = [
        ["CN", "cn"],
        ["Nu", "Nom", "Last name"],
        ["Pr", "Prenu", "Pren", "Prenom", "First name"],
        ["Ce", "Cet", "Cetățenie", "Nationalite", "Nationality"],
        ["Lo", "Loc", "Loc Naștere", "Lieu de naissance", "Place of birth"],
        ["Do", "Dom", "Domiciliu", "Adresse", "Address"]
    ]

    img = img[y + h:, x + w:x + w + 2 * w]
    img = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)
    text = pytesseract.image_to_string(img, lang="ron")
    text = os.linesep.join([s for s in text.splitlines() if s])
    arr = text.splitlines()
    curr_pat = 0
    for i in range(len(arr)):
        da = False
        for c in range(len(pattern[curr_pat])):
            if pattern[curr_pat][c] in arr[i]:
                da = True
                if curr_pat == 0:
                    inf['CNP'].set(arr[i][4:])
                elif curr_pat == 1:
                    inf['Nume'].set(arr[i + 1])
                elif curr_pat == 2:
                    inf['Prenume'].set(arr[i + 1])
                elif curr_pat == 3:
                    inf['Cetatenie'].set(arr[i + 1])
                elif curr_pat == 4:
                    inf['Loc Nastere'].set(arr[i + 1])
                elif curr_pat == 4:
                    inf['Domiciliu'].set(arr[i + 1])
                break
        if da:
            if curr_pat != len(pattern) - 1:
                curr_pat += 1
            else:
                break
    return inf


def disp(inf):
    for key, value in inf.items():
        print(key, " : ", value.get())
