import requests
import json


def message(a):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' \
          'e0d235149c06abd1874fe3c51d91713df0d5cd8569516a3f51d9be65b87ee678'
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "您的自动化测试报告已生成：%s " % (a)
        },
        "at":{
            "atMobiles":[
                "15855507106",
                "18255502181"#需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll": False #是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }
    requests.post(url, data=json.dumps(pagrem), headers=headers)

if __name__ == "__main__":
    message('自动化测试')