# -*-coding:utf8-*-
import csv
import requests
import json
import random
import sys
import datetime
import time
from imp import reload
from multiprocessing.dummy import Pool as ThreadPool
import urllib.request

def datetime_to_timestamp_in_milliseconds(d):
    def current_milli_time(): return int(round(time.time() * 1000))
    return current_milli_time()
reload(sys)


def LoadUserAgents(uafile):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[:-1])
    random.shuffle(uas)
    return uas


uas = LoadUserAgents("user_agents.txt")
head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://space.bilibili.com/45388',
    'Origin': 'http://space.bilibili.com',
    'Host': 'space.bilibili.com',
    'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}

# import socks
# import socket
#
# socks.set_default_proxy(socks.SOCKS5,"113.116.50.182",807)
# socket.socket = socks.socksocket


cc = {
    'http': 'http://124.42.7.103:80',
    'http': 'http://120.26.110.59:8080',
    'http': 'http://120.52.32.46:80',
    'http': 'http://218.85.133.62:80',
}
time1 = time.time()

urls = []


for m in range(1, 50):
    for i in range(m * 100, (m + 1) * 100):
        url = 'https://space.bilibili.com/' + str(i)
        urls.append(url)


    def getsource(url):
        payload = {
            '_': datetime_to_timestamp_in_milliseconds(datetime.datetime.now()),
            'mid': url.replace('https://space.bilibili.com/', '')
        }
        ua = random.choice(uas)
        head = {
            'User-Agent': ua,
            'Referer': 'https://space.bilibili.com/' + str(i) + '?from=search&seid=' + str(random.randint(10000, 50000))
        }
        mid = payload['mid']

        jscontent = requests \
          .session() \
          .get('https://api.bilibili.com/x/space/acc/info?mid=%s&jsonp=jsonp' % mid,
                headers=head,
                data=payload,
               proxies=cc) \
          .text

        # proxy_support = urllib.request.ProxyHandler({'sock5': '124.42.7.103:80'})
        # opener = urllib.request.build_opener(proxy_support)
        # urllib.request.install_opener(opener)
        # jscontent = urllib.request.urlopen('https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp'.format(mid)).read().decode("utf8")
        # print(jscontent)

        time2 = time.time()
        try:
            jsDict = json.loads(jscontent)
            status_code = jsDict['code'] if 'code' in jsDict.keys() else False
            if status_code == 0:
                if 'data' in jsDict.keys():
                    jsData = jsDict['data']
                    mid = jsData['mid']
                    name = jsData['name']
                    sex = jsData['sex']
                    rank = jsData['rank']
                    face = jsData['face']
                    regtimestamp = jsData['jointime']
                    regtime_local = time.localtime(regtimestamp)
                    regtime = time.strftime("%Y-%m-%d %H:%M:%S", regtime_local)

                    birthday = jsData['birthday'] if 'birthday' in jsData.keys() else 'nobirthday'
                    sign = jsData['sign']
                    level = jsData['level']
                    OfficialVerifyType = jsData['official']['type']
                    OfficialVerifyDesc = jsData['official']['desc']
                    vipType = jsData['vip']['type']
                    vipStatus = jsData['vip']['status']
                    coins = jsData['coins']
                    print("Succeed get user info: " + str(mid) + "\t" + str(time2 - time1))
                    try:
                        res = requests.get(
                            'https://api.bilibili.com/x/relation/stat?vmid=' + str(mid) + '&jsonp=jsonp').text
                        viewinfo = requests.get(
                            'https://api.bilibili.com/x/space/upstat?mid=' + str(mid) + '&jsonp=jsonp').text
                        js_fans_data = json.loads(res)
                        js_viewdata = json.loads(viewinfo)
                        following = js_fans_data['data']['following']
                        fans = js_fans_data['data']['follower']
                    except:
                        following = 0
                        fans = 0

                else:
                    print('no data now')
                try:
                    print(jsDict)

                    with open('data.csv', 'a', newline='',encoding="utf-8") as csvfile:
                        fieldnames = ['mid',
                                      'name',
                                      'sign',
                                      'sex',
                                      'birthday',
                                      'level',
                                      'following',
                                      'fans',
                                      'vipType',
                                      'vipStatus'
                                      ]
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                        # writer.writeheader()
                        writer.writerow({"mid":mid,
                                         "name":name,
                                         "sign": sign,
                                         "sex":sex,
                                         "birthday":birthday,
                                         "level":level,
                                         "following":following,
                                         "fans":fans,
                                         "vipType":vipType,
                                         "vipStatus":vipStatus
                                         })
                except Exception as e:
                    print(e)
            else:
                print("Error: " + url)
        except Exception as e:
            print(e)
            pass


        time.sleep(3)
if __name__ == "__main__":
    pool = ThreadPool(1)
    try:
        results = pool.map(getsource, urls)
    except Exception as e:
        print(e)

    pool.close()
    pool.join()