import requests
import json
import pyautogui

x = pyautogui.prompt(text='', title='' , default='')
subs= ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']


f = open(r"C:\Users\황세훈\Desktop\python_crolling\05.project1\{}.txt".format(x), 'w')

for sub in subs:
    keyword = x+' '+sub
    response = requests.get(f"https://ac.search.naver.com/nx/ac?q={keyword}&con=1&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_8")

    origin_data = response.text


    str_data= origin_data.split("_jsonp_8(" )[1][:-1] 

    dict_data = json.loads(str_data)

    dict_items_list = dict_data['items'][0]

    print(dict_items_list)


    for item in dict_items_list:
        f.write(item[0] + "\n")
        print(item[0])

f.close()



# response = requests.get("https://ac.search.naver.com/nx/ac?q=%EC%A3%BC%EC%8B%9D%20%E3%84%B1&con=1&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_8")

# keyword = "주식 ㄴ"
# response = requests.get(f"https://ac.search.naver.com/nx/ac?q={keyword}&con=1&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_8")




