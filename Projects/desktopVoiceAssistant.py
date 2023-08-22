"""Libraries installed 
    1.pip install opencv-python
    2.pip install pytesseract
    https://github.com/tesseract-ocr/tesseract - Install the tessetact exe

"""
import cv2
from PIL import Image
from pytesseract import pytesseract

camera = cv2.VideoCapture(0)

while True:
    _, image = camera.read()
    cv2.imshow('Text Detection', image)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('test1.jpg', image)
        break

camera.release()
cv2.destroyAllWindows()


def tesseract():
    path_to_tesseract = r"C: \Program Files\Tesseract-OCR\tesseract.exe"
    Imagepath = 'test1.jpg'
    pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(Image.open(Imagepath))
    print(text[:-1])


tesseract()


