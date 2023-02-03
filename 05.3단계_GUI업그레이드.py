from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

import requests
import json

subs= ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

UI_PATH = "05.project1/search.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(UI_PATH, self)

        self.start_btn.clicked.connect(self.start)
        self.reset_btn.clicked.connect(self.reset)
        self.save_btn.clicked.connect(self.save)
        self.quit_btn.clicked.connect(self.quit)

        self.save_list =[]

    def start(self):
        self.label_3.setText("추출을 시작합니다..")
        QApplication.processEvents()
        for sub in subs:
            keyword = self.item.text()+' '+sub
            response = requests.get(f"https://ac.search.naver.com/nx/ac?q={keyword}&con=1&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_8")

            origin_data = response.text


            str_data= origin_data.split("_jsonp_8(" )[1][:-1] 

            dict_data = json.loads(str_data)

            dict_items_list = dict_data['items'][0]

            for item in dict_items_list:
                self.state_message.append(item[0])
                self.save_list.append(item[0])

        self.label_3.setText("추출을 종료합니다..")

    def reset(self):
        self.state_message.setText("")
        
    def save(self):
        print(self.save_list)
        f = open(r"C:\Users\황세훈\Desktop\python_crolling\05.project1\{}.txt".format(self.item.text()), 'w')
        for item in self.save_list:
            f.write(item + "\n")
        f.close()

    def quit(self):
        sys.exit()

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())