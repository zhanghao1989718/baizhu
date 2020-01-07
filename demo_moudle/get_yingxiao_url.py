#coding:utf-8
import requests,json

def get_keywordId(showid):
    url="http://zone.bz.cn/sem/keyword/index"
    headers={"Content-Type":"application/x-www-form-urlencoded",
             "Connection":"keep-alive",
             "Content-Length":"30",
             "Host":"zone.bz.cn",
             "User-Agent":"Apache-HttpClient/4.5.2 (Java/1.8.0_221)"
             }

    request_param={
        "urrPage":"1",
        "pageSize":"20",
        "showId":showid
    }
    # response=requests.post(url,data=json.dumps(request_param), headers=headers)
    response=requests.post(url, data = request_param, headers = headers)

    get_text = response.text
    # json.loads把json格式转换为python识别的格式
    # print(json.loads(get_text)["content"]["pageContent"][1]["keywordId"])
    # print(get_text)
    print(json.loads(get_text)["content"]["pageContent"][1]["showId"])
    print("=" * 50)
    return json.loads(get_text)["content"]["pageContent"][1]["keywordId"]


def get_url(showid):
    url = "http://zone.bz.cn/sem/keyword/show"
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               "Connection": "keep-alive",
               "Content-Length": "30",
               "Host": "zone.bz.cn",
               "User-Agent": "Apache-HttpClient/4.5.2 (Java/1.8.0_221)"
               }

    request_param = {
        "keywordId": get_keywordId(showid)

    }
    response = requests.post(url, data=request_param, headers=headers)

    get_text = response.text
    print(json.loads(get_text)["data"]["keyword"]["destinationUrl"])
    return json.loads(get_text)["data"]["keyword"]["destinationUrl"]

if __name__ == "__main__":
    get_url(8)