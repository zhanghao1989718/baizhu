from urllib import parse

s = '__guid=98192282.207200161544257820.1573732895543.8887; ci_session=a%3A11%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22714afeeae3ce471463447b2fa345306f%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A13%3A%22183.163.166.4%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A110%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+WOW64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F63.0.3239.132+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1576549000%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A3%3A%22uid%22%3Bs%3A3%3A%22387%22%3Bs%3A5%3A%22uname%22%3Bs%3A8%3A%22zhanghao%22%3Bs%3A5%3A%22level%22%3Bs%3A1%3A%220%22%3Bs%3A6%3A%22appids%22%3Bs%3A1%3A%220%22%3Bs%3A6%3A%22roleid%22%3Bs%3A1%3A%221%22%3Bs%3A9%3A%22open_time%22%3Bs%3A19%3A%222019-05-14+17%3A10%3A21%22%3B%7Df2455a6a6347ed579644365cd23e138b3076dd0f; monitor_count=11'
a = parse.unquote(s)
print(a)