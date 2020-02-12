from PIL import Image
import pytesseract
from getreturnnum import vci

# 打开图片，需要安装tesseract-ocr
imageObject =Image.open('C:\\Users\\80649.LAPTOP-T3EKEB7M\\Desktop\\1.png')
print (imageObject)
print (pytesseract.image_to_string(imageObject))



# 识图网站识别
# img = Image.open(img_path)
# result = vci.base64_api(uname='zhanghao1989718', pwd='1989718', img=img)
# print(result)
