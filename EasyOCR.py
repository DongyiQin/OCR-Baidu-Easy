import pytesseract
from PIL import Image
img = Image.open('exo.jpg')
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\dell\Desktop\TextBook_\手工工作\知识清单OCR\tesseract\Tesseract-OCR\tesseract.exe'
s = pytesseract.image_to_string(img, lang='chi_sim')  #不加lang参数的话，默认进行英文识别
print(s)
