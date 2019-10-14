# _*_ coding:utf-8 _*_
import requests
import json

# 百助测试部门token
# https://oapi.dingtalk.com/robot/send?access_token=273e79e103fd6d5705fcb6a6282df47640efdd047457dfc56a00ba620cd2c1d9
# 测试用
# https://oapi.dingtalk.com/robot/send?access_token=e0d235149c06abd1874fe3c51d91713df0d5cd8569516a3f51d9be65b87ee678
def message(a):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' \
          'e0d235149c06abd1874fe3c51d91713df0d5cd8569516a3f51d9be65b87ee678'
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "桔梗软件站：%s " % (a)

        },
        "at":{
            "atMobiles":[
                "",
                ""#需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll": True #是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }
    requests.post(url, data=json.dumps(pagrem), headers=headers)


if __name__ == "__main__":
    message('自动化测试')