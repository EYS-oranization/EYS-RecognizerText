from PIL import Image
import pytesseract
import cv2
import os

image = 'tests/test1.png'

text = pytesseract.image_to_string(Image.open(image))
print(text)