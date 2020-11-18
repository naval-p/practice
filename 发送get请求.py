'''
发送get请求
'''

import requests

# 发送一个get请求,re是收到的响应
# 接口地址  http://www.baidu.com
re = requests.get("http://www.baidu.com")
# 文本格式的响应内容、
print(re.text)
# 响应码
print(re.status_code)
assert re .status_code == 200
# ok
print(re.reason)

assert re.reason == "OK"

r = requests.get("http://jy001:8081/futureloan/mvc/api/loan/audit?id=1&status=4")
print(r.text)

print(r.status_code)
assert r.status_code == 200

print(r.reason)
assert r.reason == "OK"

assert r.json()['status'] == 0
assert r.json()['code'] == '20207'

# get请求带参数
# 方法1:拼接到url后面
rr = requests.get("http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=136791&pwd=123456&regname=didiiddi")
print(rr.text)

print(rr.status_code)
assert rr.status_code == 200

print(rr.reason)
assert rr.reason == "OK"

# assert r.json()['status'] == 0
# assert r.json()['code'] == '20109'
# 方法2:使用params传参
url = "http://jy001:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone":"13645987521","pwd":"123456","regname":"Nasa"}
r = requests.get(url,params=canshu)
print(r.text)
print(r.status_code)

# get 请求带请求头
url = "https://wenku.baidu.com/view/027d607deff9aef8941e06c0.html"
r = requests.get(url) #"User-Agent": "python-requests/2.24.0",
print(r.text)

tou = {
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63"}
r = requests.get(url,headers = tou)
print(r.text)