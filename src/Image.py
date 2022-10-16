import mss
import pytesseract
from PIL import Image


def saveScreenshot(img_path, x1, x2, y1, y2):
    with mss.mss() as sct:
        monitor = {"top": y1, "left": x1, "width": x2 - x1, "height": y2 - y1}
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=img_path)


def readImage(img_path):
    return pytesseract.image_to_string(Image.open(img_path))
