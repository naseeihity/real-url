# 获取网易云音乐旗下look直播的真实流媒体地址。
# look直播间链接形式：https://look.163.com/live?id=73694082


import requests
import re
import json


def get_real_url(rid):
    real_url = []
    try:
        response = requests.post(
            url='https://look.163.com/live?id=' + rid).text
        urls = re.findall(r'"liveUrl":([\s\S]*),"liveType"', response)[0]
        urls = json.loads(urls)
        real_url.append(urls['httpPullUrl'])
        real_url.append(urls['hlsPullUrl'])
        real_url.append(urls['rtmpPullUrl'])
    except:
        real_url = '该直播间不存在或未开播'
    return real_url


if __name__ == "__main__":
    rid = input('请输入look直播房间号：\n')
    real_url = get_real_url(rid)
    print('该直播间源地址为：')
    print(real_url)
