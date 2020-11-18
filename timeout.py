'''
timeout
1.接口性能测试比如某个接口在500ms内返回
2.耗时比较久的操作,默认的超时时间执行不完,比如上传超大文件,可以设置大一点的超时时间


import requests
url = 'https://tcc.taobao.com/cc/json//mobile_tel_segment.htm?tel=17695462837'
#1s = 1000ms
for i in range(10):
    try:

        r = requests.get(url,timeout = 0.1)
        print(r.text)
    except Exception as e:
        print(e)
'''
'''
proxies 代理
1.通过代理抓包,用fiddler抓自动化发的报文分析
2.当ip被服务器屏蔽后,可以通过代理换个ip继续访问.
'''
import  requests
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}

#shezhi proxies参数时,要打开代理服务器,例如fiddler
r = requests.get("http://www.baidu.com",proxies = proxy)
print(r.text)

r = requests.get("https://www.bagevent.com",proxies = proxy,verify = False,timeout = 0.5)
print(r.text)