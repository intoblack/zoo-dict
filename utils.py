#coding=utf-8




import urllib2
import urllib
import json
import random
import time
import os
from ZooException import ZooException

code = {"gbk":"gbk",\
        "utf-8":"utf-8"}


_jload = json.loads
_urlencode = urllib.urlencode


def cls():
    os.system("cls")
    
def get_url_data(url , data = None,codemode = "gbk"):
    html = ""
    if not code.has_key(codemode):
        raise ZooException("NO_RIGHT_DECODE",101)
    if data:
        req = urllib2.Request(url)
        html = urllib2.urlopen(req,data).read().decode(codemode)
    else:
        req = urllib2.Request(url)
        html = urllib2.urlopen(req).read().decode(codemode)
    return html


def jsonstrtodict(jsonstr):
    datadict = None
    try:
        datadict = _jload(jsonstr)
    except Exception,e:
        raise  ZooException("JSON_DECODE_ERRO_%s" % e , 102)
    return datadict

def queryurl(baseurl,querydict):
    return "%s%s" % (baseurl,_urlencode(querydict))

'''
函数名称： randint
函数功能： 随机生成n位随机数
参数列表：
       n 随机生成的位数
返回值：
       整数型
'''
def randint(n):
    _num = 1
    if n > 1:
        for i in range(n - 1):
            _num *= 10
    else:
        raise ZooException("NO_RIGHT_NUM",110)
    return random.randint(_num,(_num * 10) - 1)

def clear_data(data):
    re_data = ''
    if data and len(data)>2:
        re_data = data[data.index("(") + 1:data.rindex(")")]
    return re_data

def randintbyrang(_min,_max):
    if _min >= _max:
        raise ZooException("VALUE_IS_NOT_VALUE",113) 
    return random.randint(_min,_max)

def timems():
    return long(time.time()) * 1000


def getksTs():
    return "%s_%s" % (timems(),randint(4))

def getJsonp():
    return "jsonp%s" % (randint(4))





