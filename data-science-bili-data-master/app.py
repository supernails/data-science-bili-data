#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site :
# @Describe:

from flask import Flask, render_template
from data import SourceData

app = Flask(__name__)

'''
定义了3个网址，用同一套模板渲染
'''


@app.route('/')
def index():
    # 新建一个实例
    data = SourceData()
    # 传入一个实例，和实例的标题
    return render_template('index.html', form=data, title=data.title)


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=False)
