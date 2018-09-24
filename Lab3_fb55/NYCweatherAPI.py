from __future__ import print_function#python 3引到2
import json #包
try:#改包的名字
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os# 管理文件路径的python包 读取文件路径 环境变量
import sys #管理参数


apikey = os.getenv("WEATHERAPIKEY")#api内置
mode = "Json"
units = "metric"
city = sys.argv[1]

url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&mode=%s&units=%s&cnt=7&APPID=%s"%(city, mode, units, apikey)#分装成的样式

print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)


print (dataDict)

