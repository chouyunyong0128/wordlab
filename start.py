# -*- coding:utf-8 -*- #
from __future__ import print_function
import os
from time import sleep
import re, json, logging
from flask import Flask, url_for, redirect, render_template, request, flash
import webbrowser


app = Flask(__name__)


is_sort = False

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def read_data(filename):    # read data from database
    with open(f'./database/{filename}', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    words = {}
    for line in lines:
        line = line.strip()
        if line != '':
            data = [d.strip() for d in line.strip().split('@')]
            # english : englisg, 中文, collcation...
            words[data[0]] = data

    if is_sort:
        # 針對 key 進行排序
        words = sorted(words.items(), key=lambda it: it[0])
        # 重新組織成 dictionary
        words = {k:v for (k,v) in words}

    return words

# 透過 render_template 載入 html
@app.route('/toeic')
def toeic():
    
    return render_template('toeic.html', word_dict=read_data('toeic.txt'))

# 工作單字
@app.route('/work')
def work():
    # 取讀單字清單
    
    return render_template('work.html', word_dict=read_data('work.txt'))


# 加入新單字
@app.route('/add')
def add():
    return render_template('add_toeic.html')


if __name__ == '__main__':

    # app.debug = True
    # app.run(debug=True, host='0.0.0.0', port=8090, processes=1)
    print(f"web address: http://127.0.0.1:8090/toeic")
    print(f"web address: http://127.0.0.1:8090/work")
    app.run(debug=True, host='0.0.0.0', port=8090)
    # app.run()


  
    