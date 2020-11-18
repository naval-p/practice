from datetime import datetime
from time import sleep
import psutil
with open("d:/资源占用详情.txt",encoding='utf-8',mode='a')as file:
    file.write("时间戳\t               cpu%\t 内存%\t 磁盘%\t  发送字节数\t接受字节数\t \n")
    while(True):
        print("监控信息")
        file.write(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S") + "\t")
        file.write(str(psutil.cpu_percent()) + "%\t")
        file.write(str(psutil.virtual_memory().percent) + "%\t")
        file.write(str(psutil.disk_usage("d:/").percent) + "%\t")
        file.write(str(psutil.net_io_counters().bytes_sent) + "\t")
        file.write(str(psutil.net_io_counters().bytes_recv) +"\n")
        file.flush()
        sleep(3)


        '''
        print(psutil.cpu_percent())#获取cpu信息
        print(psutil.virtual_memory())#虚拟内存
        print(psutil.virtual_memory().percent)#虚拟内存百分比
        print(psutil.disk_usage("d:/"))#租车系统所在的盘
        print(psutil.disk_usage("d:/").percent)#租车系统所在盘的百分比
        print(psutil.net_io_counters())#网络
        print(psutil.net_io_counters().bytes_sent)#发送的字节数
        print(psutil.net_io_counters().bytes_recv)#接受的字节数
        '''


