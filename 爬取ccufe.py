
# coding: utf-8

import re
import urllib
import urllib2
import cookielib



loginUrl = 'http://edu.*.cc/Grade/SStudentGradeSelect.aspx'


#cookie
cookie =cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)


#postdata
values = {
    'cobRole': '*',
    'User_ID': '*',
    'User_Pass': '*',
    'txtVolidate': ''
}
postdata = urllib.urlencode(values)


#headers
header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Referer':'http://edu.*.cc/'
}


#第一次请求网页得到cookie
request = urllib2.Request(loginUrl,postdata,headers=header)
response = opener.open(request)
print'第一次请求网页得到cookie:'
print response.getcode()

#获取验证码----------------!!!问题一直出在这，要用带cookie的方法访问验证码的网页---这样的话进入的验证码的页面对应的验证码就是登陆页面的验证码了哈哈哈哈哈(之前用的是不带cookie的urlopen()方法...)
yzm = opener.open('http://edu.*.cc/VerifyCode.aspx?')
yzm_data =  yzm.read()
yzm_pic = file('/Users/so/Desktop/yzm.jpeg','wb')
yzm_pic.write(yzm_data)
yzm_pic.close()


#用户输入验证码
print ('请输入验证码：')
values['txtVolidate'] = raw_input()


#带验证码模拟登陆
postdata = urllib.urlencode(values)
request = urllib2.Request(loginUrl,postdata,header)
response = opener.open(request)
print 'Response of loginAction.do'
print response.read().decode('utf-8')





