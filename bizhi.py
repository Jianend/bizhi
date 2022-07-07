'''访问网站'''

import ctypes
import os
import requests
import time







'''josn'''
import json
def get_json(url):
    try:
        hasattr = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Mobile Safari/537.36 Edg/103.0.1264.44'}
        r = requests.get(url, headers=hasattr)
        return r.json()
    except:
        print('完成')
        return 0

def get_soup(url):
    url=url['data']
    url=url[0]
    jpg=url['ext']
    url=url['pid']
    surl='https://pximg.rainchan.win/img?img_id='+str(url)
    name=get_img(surl,'a.'+jpg)
    return name


'''下载图片'''
def get_img(url,name):
    try:
        hasattr = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Mobile Safari/537.36 Edg/103.0.1264.44'}
        r = requests.get(url, headers=hasattr)
        with open(name, 'wb') as f:
            f.write(r.content)
            f.close()
        return name
    except:
        print('完成')
        return 0      
    


    
if __name__  == "__main__":
    url = 'https://api.lolicon.app/setu/v2?r18=1'
    html=get_json(url)
    name = get_soup(html)
    
    '''当前目录'''
    
    ml=os.getcwd()+'\\'+name

    '''设置背景图片a.jpg'''
    ctypes.windll.user32.SystemParametersInfoW(20, 0, ml, 0)
    print('成功')
    '''设置背景图片a.jpg'''
    '''倒计时'''
    sum = 60         # 设置倒计时时间
    timeflush = 0.25  # 设置屏幕刷新的间隔时间
    a=int(sum/timeflush)
    for i in range(0, a):
        list = ["\\", "|", "/", "—"]
        index = i % 4
        print("\r程序正在运行 {}".format(list[index]), end="")
        time.sleep(timeflush)
    #git  pull
    os.system('git add . ')
    os.system(' git commit -m "bz"')
    os.system('git push -u origin main')
    p='python '+__file__
    os.system(p)