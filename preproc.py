import cv2
import numpy as np


def canny(image):
    return cv2.Canny(image, 100, 200)


def preprocesare(file):
    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return img
