# Real-Url

## Real-url for Alfred + IINA workflow

```
zb {platfrom} {room id}

Example:
zb douyu 9999
```

## Features
- [x] Open any platform live poadcast in IINA by room id
- [ ] show room info in playlist
- [ ] add room into a local playlist and save it
- [ ] open a playlist with all added rooms

## Not support now
17live
Douyin
qie
Kuaishou

## 说明

这个仓库存放的是：获取一些直播平台真实流媒体地址（直播源）的 Python 代码实现。获取的地址均可在 PotPlayer、VLC 播放器中播放，部分可在 flv.js 中播放。

目前整理了 **26** 个直播平台：斗鱼直播、虎牙直播、哔哩哔哩直播、战旗直播、网易 CC 直播、火猫直播、企鹅电竞、YY 直播、一直播、快手直播、花椒直播、映客直播、西瓜直播、触手直播、NOW 直播、抖音直播，爱奇艺直播、酷狗直播、龙珠直播、PPS 奇秀直播、六间房、17 直播、来疯直播、优酷轮播台、网易 look 直播、千帆直播。

## 运行

1. 项目使用了很简单的 Python 代码，仅在 Python 3 环境运行测试。
2. 具体所需模块请查看代码中的 import。
3. 爱奇艺直播里有个参数是加盐的 MD5，使用仓库中的 iqiyi.js。

