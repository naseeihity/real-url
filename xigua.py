# 获取西瓜直播的真实流媒体地址。


import requests
import re
import json


def get_real_url(rid):
    try:
        room_url = "https://live.ixigua.com/" + rid
        response = requests.get(url=room_url).text
        real_url = re.findall(r'playInfo":([\s\S]*?),"authStatus', response)[0]
        real_url = json.loads(re.sub(r'\\u002F', '/', real_url))
        if len(real_url) > 0:
            real_url = real_url[0]['FlvUrl']
        else:
            real_url = "url not found"
    except:
        real_url = '直播间不存在或未开播'
    return real_url


if __name__ == "__main__":
    rid = input('请输入西瓜直播URL：\n')
    real_url = get_real_url(rid)
    print('该直播源地址为：')
    print(real_url)
