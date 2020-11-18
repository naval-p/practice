'''
发送post请求:带参数
1.data传参
2.json传参
'''

import requests
import json
url = "http://jy001:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone":"13013026068","pwd":"123456"}
r= requests.post(url,json = canshu )#系统不支持json方式传参
print(r.text)
r = requests.post(url,data = canshu )
print(r.text)

r =requests.post("http://www.httpbin.org/post", data = canshu)#"Content-Type": "application/x-www-form-urlencoded"
print(r.text)
r = requests.post("http://www.httpbin.org/post", json = canshu)#"Content-Type": "application/json"
print(r.text)