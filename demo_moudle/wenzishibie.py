import os
from aip import AipOcr

""" API """
APP_ID = 'a9b15483e4324e1ea96305f3820fea71'
API_KEY = 'QR8z0EI4NLIYBMitxHzjADhx'
SECRET_KEY = '6j1ndFYRpg3XK6IVaaVhdZxw9XfPBwTW'
# 初始化AipFace对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


class AipOcr(object):

    def __init__(self, filepath):
        self.filepath = filepath

    """ 读取图片 """
    def get_file_content(self):
        with open(self.filepath, 'rb') as fp:
            return fp.read()

    def img_to_str(self):

        """ 可选参数 """
        options = {}
        options["language_type"] = "CHN_ENG"  # 中英文混合
        options["detect_direction"] = "true"  # 检测朝向
        options["detect_language"] = "true"  # 是否检测语言
        options["probability"] = "false"  # 是否返回识别结果中每一行的置信度

        image = self.get_file_content()

        """ 带参数调用通用文字识别 """
        result = client.basicGeneral(self.get_file_content(), options)

        # 格式化输出-提取需要的部分
        if 'words_result' in result:
            text = ('\n'.join([w['words'] for w in result['words_result']]))

            # print(type(result), "和", type(text))
            # print(image)

            """ save """
            fs = open(os.path.join(os.path.expanduser('~'), "Desktop") + "baidu_ocr.txt", 'w+')  # 将str,保存到txt
            fs.write(text)
            fs.close()
            return text

    def run(self):
        self.get_file_content()
        self.img_to_str()
        print(self.img_to_str())

if __name__ == '__main__':
    ao = AipOcr(filepath = (os.path.abspath(".")+"\png.png"))
    ao.run()
    print("识别完成。")