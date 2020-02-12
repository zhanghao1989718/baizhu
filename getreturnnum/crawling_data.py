from PIL import Image
import pytesseract

imageObject =Image.open('C:\\Users\\80649.LAPTOP-T3EKEB7M\\Desktop\\2.png')
print (imageObject)
print (pytesseract.image_to_string(imageObject))