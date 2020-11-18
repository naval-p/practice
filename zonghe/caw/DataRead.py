'''
读文件的方法

'''
import configparser
import os

import yaml


def getProjectPath():
    '''
    获取当前工程的路径
    :return:
    '''
    current__file__path = os.path.realpath(__file__)#文件所在路径
    # print(current__file__path)
    dir_name = os.path.dirname(current__file__path)#文件所在目录
    # print(dir_name)
    dir_name = os.path.dirname(dir_name)#上一级目录
    # print(dir_name)
    dir_name = os.path.dirname(dir_name)#上一级目录
    return dir_name +"\\"


def readini(filepath,key):
    '''
    读取ini文件
    :param filepath:文件路径
    :param key:ini中的关键字
    :return:key对应的value
    '''
    real_path = getProjectPath() + filepath
    #调用configparser来解析配置文件
    config = configparser.ConfigParser()
    #读文件
    config.read(real_path)
    value = config.get("env",key)
    return value
def readyaml(filepath):
    '''
    :param filepath: 文件路径
    :return: yaml文件的内容
    '''
    real_path= getProjectPath()+filepath
    with open(real_path,"r",encoding="utf-8")as f:#打开yaml文件
        content = yaml.load(f, Loader=yaml.FullLoader)#读取文件内容
        return content
'''
if __name__ == '__main__':
    print(getProjectPath())
    r = readini(r"zonghe/data_env/env.ini","url")
    print(r)
    w = readini(r"zonghe/data_env/env.ini","db")
    print(w)
    content = readyaml(r"zonghe/data_case/register_pass.yaml.yaml")
    print(content)
'''

