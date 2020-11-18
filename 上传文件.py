'''
上传文件:post,files参数上传文件
files参数是字典的格式

'''
import requests

url = "http://www.httpbin.org/post"
'''
files参数:字典的格式,"name":file-tuple
file-tuple可以说2-tuple('filename',fileobj) 3-tuple
'''

#上传文件
with open("D:/test.txt",encoding="utf-8")as f:
    file = {"file1":("text.txt",f,"text/plain")}#file1(接口参数名称)
    r = requests.post(url,files = file)
    print(r.text)
    print(r.status_code)


#上传图片
with open("D:/111.png",mode ="rb")as h:
    png = {"file1":("111.png",h,"image/png")}

    r = requests.post(url,files = png)
    print(r.text)



file = {
  "field1" : [
                 ("filename1", open("D:/test.txt", "rb"),"text/plain"),
                 ("filename2", open("D:/111.png", "rb"), "image/png"),
               ]
}
r = requests.post(url,file)
print(r.text)
print(r.status_code)