from System import *
from Image import *
from Achievements import *
from Normalize import *

user = input("Windows Username : ")
pytesseract.pytesseract.tesseract_cmd = f"C:\\Users\\{user}\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
img_path = "..\\res\\Tmp.png"
file_path = "..\\output\\YourAchievements.txt"
achievements = ""

deleteFile(file_path)
convertSrcAchievements()

print("Don't forget to :")
print("1 - Find \"Wonders of the World\" achievements list.")
print("2 - Scroll the list to the last completed achievement.")
input("Press Enter.")

x1, y1 = getClick("Click on the Circle 1 as shown in the picture on GitHub.")
time.sleep(0.4)
x2, y2 = getClick("Click on the Circle 2 as shown in the picture on GitHub.")
time.sleep(0.4)

print("Do not move your mouse during the process !")
time.sleep(4)

pyautogui.moveTo(x2, y2)

more = True
while True:
    saveScreenshot(img_path, x1, x2, y1, y2)
    text = readImage(img_path)
    titles = normalizeString(text)

    if titles in achievements:
        break

    achievements += titles
    with open(file_path, "a+", encoding="utf-8") as text_file:
        text_file.write(titles)

    for i in range(0, 48):
        pyautogui.scroll(-1)

    if more is True:
        pyautogui.scroll(-1)
        more = False
    else:
        more = True

    time.sleep(1)

deleteFile(img_path)
getNotCompletedAchievementsV2(file_path)

print("Finished.")
