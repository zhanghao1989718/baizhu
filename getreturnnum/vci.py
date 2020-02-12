import json
import requests
import base64
from io import BytesIO
from PIL import Image
from sys import version_info


def base64_api(uname, pwd, img):
    img = img.convert('RGB')
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    if version_info.major >= 3:
        b64 = str(base64.b64encode(buffered.getvalue()), encoding='utf-8')
    else:
        b64 = str(base64.b64encode(buffered.getvalue()))
    data = {"username": uname, "password": pwd, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


if __name__ == "__main__":
    img_path = "C:\\Users\\80649.LAPTOP-T3EKEB7M\\Desktop\\2.png"
    img = Image.open(img_path)
    result = base64_api(uname='zhanghao1989718', pwd='1989718', img=img)
    print(result)
