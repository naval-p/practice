import requests
'''
str ="2780487875@qq.com"
head = {
    "Cookie:"" SESSION=796fae18-ed57-4982-b0f9-8cfabfc6da26; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1604643762; __auc=d459fe061759c38afba5f8f1672; MEIQIA_TRACK_ID=1juAmY6kTltDOm2BU0zeSwPSvHC; _ga=GA1.2.392720944.1604643768; _gid=GA1.2.397703840.1604643768; __asc=d6501ea81759c8b18774d6b3610; MEIQIA_VISIT_ID=1juLjTtuPoBQvwTbGk4JFOP0d2G; BAGSESSIONID=38bb368d-a31b-4b6b-9572-417331c80063; JSESSIONID=E8EC8A6C9E3CD5253D7BADF81AE3830D; _gat=1; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1604649198; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_=%s; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af3%str"

    }
r = requests.get("https://www.bagevent.com/account/dashboard",headers = head)
print(r.text)'''

'''
requests中的cookies的自动管理机制
'''
#创建一个session,通过session来发送请求
s = requests.session()
print("登录之前的cookies:",s.cookies)
#登录
canshu = {
    "access_type":1,
    "loginType":1,
    "emailLoginWay":0,
    "account":"18710            698529",
    "password":"kiss2310027",
    "remindmeBox":"on",
    "remindme":1
}
r =s.post("https://www.bagevent.com/user/login",data = canshu)
# print(r.text)
print("登录之后的cookies:",s.cookies)
#调用dashbord接口
r = s.get("https://www.bagevent.com/account/dashboard")
# print(r.text)
print("<title>百格活动 - 账户总览</title>"in r.text)