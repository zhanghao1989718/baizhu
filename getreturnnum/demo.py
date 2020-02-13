import json
import requests
url = "https://dm.iqiyi.com/pcfirm/clt/actives"
headers = {
		   "Content-Type": "application/json;charset=UTF-8",
		   "Connection": "keep-alive",
		   "Cookie":"JSESSIONID=35E8CB641DBC9109387153498157BBFD; T00404=93b34a2cde7df4a87bda6d00171e7c0c; __guid=188201405.4112778900262155000.1581492408719; monitor_count=10"
		   }
request_param = {
				 "user_id": "326",
				 "fromDate": "2020-01-30",
				 "toDate": "2020-02-05",
				 "Host":"dm.iqiyi.com",
				 "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"

				 }
# response=requests.post(url,data=json.dumps(request_param), headers=headers)
response = requests.post(url, data=request_param, headers=headers)
get_text = response.text
print(get_text)


