# -*- coding:utf-8 -*-
import requests
import json
import time


account = "xxxxx" #学号
password = "xxx" #密码
school_id = "7" #学校ID
address = "%E6%B1%9F%E8%8B%8F%E7%9C%81%E5%8D%97%E4%BA%AC%E5%B8%82%E6%B1%9F%E5%AE%81%E5%8C%BA%E4%B8%9C%E5%90%89%E5%A4%A7%E9%81%93%E9%9D%A0%E8%BF%91%E6%B1%9F%E8%8B%8F%E8%BD%AF%E4%BB%B6%E5%9B%AD%E4%B8%9C%E6%96%B9%E6%A5%BC" #江苏省南京市江宁区东吉大道靠近江苏软件园东方楼
latitude = "31.828957" #纬度信息
comment = "%E5%AE%9E%E4%B9%A0%E5%9F%B9%E8%AE%AD" #实习培训
longitude = "118.773201" #经度信息

urllogin = 'https://api.xixunyun.com/login/admin'
payloadlogin = 'account=' + account + '&password=' + password + '&school_id=' + school_id + '&request_source=1'
headerlogininfo = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8','Accept': 'application/json, text/javascript, */*; q=0.01','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0','Referer': 'https://www.xixunyun.com/login.html','Origin': 'https://www.xixunyun.com' }
w = requests.post(urllogin, data=payloadlogin, headers=headerlogininfo)

# 调试
# print url,payload
# print urllogin,payloadlogin,headerlogininfo

print '*'*60
print u'\u767b\u5f55\u5185\u5bb9\uff1a'.encode('gbk')
print w.text
print '*'*60
loginmsg = json.loads(w.text)
logintoken = loginmsg['data']['token']
loginstatus = loginmsg['message']
print u'\u767b\u5f55\u72b6\u6001\uff1a'.encode('gbk')
print loginstatus
print '*'*60
print u'token\u503c\uff1a'.encode('gbk')
print logintoken
print '*'*60


token = logintoken


url = 'https://api.xixunyun.com/signin?platform=android&version=3.3.3&token=' +  token + '&entrance_year=0&graduate_year=0'
payload = 'address=' + address + '&latitude=' + latitude + '&comment=' + comment + '&sign_type=0&longitude=' + longitude
headerinfo = {'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Power_By_wrysunny' }
r = requests.post(url, data=payload, headers=headerinfo)

print '*'*60
print u'\u72b6\u6001\u7801\uff1a'.encode('gbk')
print r.status_code
print '*'*60
msg = json.loads(r.text)
msgdecode = msg['message']
print msgdecode.encode("gbk")
print '*'*60
print r.text
print '_'*60
print 'now time :'
print time.time()
print '_'*60
