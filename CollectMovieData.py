import http.client
import json
import time
import sys
import collections
import urllib.parse

# #API = ‘723ce9c35b6115f71d797a5b10be6057’
# request_url = "http://www.tuling123.com/openapi/api"
# conn = http.client.HTTPConnection('www.tuling123.com')
# header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
# conn.request(method="POST", url=request_url, headers=header, body=test_data_url_encode)
# print(conn)
# response = conn.getresponse()
# #print(response.status)
# #print(response.reason)
# res = response.read()
# print(res)

conn = http.client.HTTPSConnection("api.themoviedb.org")

data = {
    'api_key': '723ce9c35b6115f71d797a5b10be6057',
    'language':'en-US',
    'sort_by':'popularity.desc',
    'page':1
}

# 将字典转化为query_string
query_string = urllib.parse.urlencode(data)
print(query_string)

# 指定 request 请求的方法和请求的链接地址

conn.request("GET",'/3/discover/movie?'+query_string)
response = conn.getresponse()
#print(response.status)
#print(response.reason)
res = response.read().decode()
print(res)