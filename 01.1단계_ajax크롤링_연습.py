import requests
import json

response = requests.get("https://ac.search.naver.com/nx/ac?q=%EC%A3%BC%EC%8B%9D%20%E3%84%B1&con=1&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_8")

origin_data = response.text


print(origin_data.split('_jsonp_8(')[1][:-1])

#dict 형태로 변경
str_data = origin_data.split('_jsonp_8(')[1][:-1]
print(type(str_data))

#str -> dict으로 자료형 변환
dic_data = json.loads(str_data)
print(type(dic_data))
