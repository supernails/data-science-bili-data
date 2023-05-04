import requests  # 用于得到网页链接
from bs4 import BeautifulSoup  # 引入解析块儿
import datetime  # 用于得到当前时间
import time  # 用于程序延时
import json  # 用于解析JSON格式的库
import pandas as pd


def write_csv_line_by_line(array):
    df = pd.DataFrame(array)
    # df.to_csv('res.csv', header=False)  # 不加表头
    df.columns = ['time', 'mid', 'name', 'sex', 'sign', 'level']
    df.to_csv('res.csv', mode='a', index=False, header=False)  # 添加表头


def get_fans(Name=None):
    print(Name)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
    # if Name == None:
    #     print("未输入姓名，请重新运行")
    #     return
    try:
        # 储存粉丝数
        # response_0 = requests.get('https://api.bilibili.com/x/relation/stat?vmid=' + str(Name) + '&jsonp=jsonp',
        #                           headers=headers)
        # 储存UP名字
        response_1 = requests.get('https://api.bilibili.com/x/space/acc/info?mid=' + str(Name) + '&jsonp=jsonp',
                                  headers=headers)
    # 网络连接失败
    except:
        with open('B站粉丝数.txt', 'a', encoding='utf-8') as f:
            # 输出爬取时间
            f.write("\n")
            f.write(str(datetime.datetime.now()) + '\n')  # 此处可能与爬取内容时有微小的时间差
            f.write("连接网络失败")
            f.write("\n")
    # 成功得到网页
    else:
        response_1_text = response_1.text
        if response_1_text[8:12] == '-509':
            # 请求过于频繁，请稍后再试
            response_1_text = response_1_text[46:]
        # J_data_0 = json.loads(response_0.text)
        J_data_1 = json.loads(response_1_text)
        if J_data_1['code'] == 0:
            # with open('B站粉丝数.txt', 'a', encoding='utf-8') as f:
            # f.write(str("时间：" + str(datetime.datetime.now()) + '\n' +
            #             "UP：" + str(J_data_1['data']['name']) + '\n' +
            #             "粉丝数：" + str(J_data_0['data']['follower']) + '\n\n'))
            # ['time', 'mid', 'name', 'sex', 'sign', 'level']
            dataArray = [str(datetime.datetime.now()), Name, str(J_data_1['data']['name']),
                         str(J_data_1['data']['sex']), str(J_data_1['data']['sign']), str(J_data_1['data']['level'])]
            write_csv_line_by_line([dataArray])
        else:
            print("mid:{0},无对应用户".format(Name))


def main(i):
    get_fans(i)


if __name__ == '__main__':
    # get_fans(42)
    for i in range(3402, 500000000, 100):
        get_fans(i)
        time.sleep(2)
    # file = open("./reponse.txt", 'r', encoding='utf-8')
    # responseText = file.read()
