import json
import sys
import requests
import subprocess
from GetUrl import GetUrl

RoomList = 'roomlist.json'
PlatList = "playlist.m3u8"

def get_douyu_room_info(id):
    url = "http://open.douyucdn.cn/api/RoomApi/room/{}".format(id)

    room_name = ""
    owner_name = ""
    try:
        response = requests.get(url)
        response = response.json()
        if response.get('error') == 0:
            room_name = (response.get('data')).get('room_name')
            owner_name = (response.get('data')).get('owner_name')
    except:
        room_name = "Failed"
        owner_name = "UKN"

    return room_name, owner_name


def get_room_list(roomset):
    rooms = []
    for platform, rid in roomset:
        owner_name = platform
        room_name = rid
        if platform == 'youku':
            url, room_name = get_real_url_by_platform(platform, rid)
        else:
            url = get_real_url_by_platform(platform, rid)
        if isinstance(url, type([])) and len(url) > 0:
            url = url[0]
        if url is None or not url.startswith('http'):
            continue
        if platform == "douyu":
            room_name, owner_name = get_douyu_room_info(rid)
        rooms.append({"name": owner_name+"_"+ str(room_name), "url": url})
    return rooms


def generate_play_list(rooms):
    with open(PlatList, mode="a", encoding='utf-8') as f:
        f.seek(0)
        f.truncate()
        for room in rooms:
            info = "#EXTINF:-1,{}\n".format(room["name"])
            f.write(info)
            url = room["url"] + "\n"
            f.write(url)
    f.close()

def open_iina():
    subprocess.call(["open", PlatList])

def get_real_url_by_platform(platform, rid):
    get_url_funcs = GetUrl()
    get_real_url = getattr(get_url_funcs, platform)
    if platform == 'youku':
        url, name = get_real_url(rid)
        return url, name
    else:
        url = get_real_url(rid)
    print("Get url succeed:", url)
    return url


def get_room_ids(platform=''):
    all_rooms = []
    with open(RoomList, mode="r", encoding='utf-8') as f:
        data = json.load(f)
        all_rooms = [(group, rid) for group in data for rid in data[group]]
        if len(platform) > 0:
            all_rooms = [room for room in all_rooms if room[0] in platform]
    f.close()
    return all_rooms


def add_room_ids(platform, ids):
    def get_rooms():
        with open(RoomList, mode="r", encoding='utf-8') as f:
            data = json.load(f)
            id_list = ids.split(',')
            if platform not in data:
                data[platform] = []
            data[platform].extend(id_list)

        f.close()
        return data

    def rewrite(rooms):
        with open(RoomList, 'w') as f:
            json.dump(rooms, f)
        f.close()

    rooms = get_rooms()
    rewrite(rooms)


def update_play_list(rooms, play=False):
    playlists = get_room_list(rooms)
    generate_play_list(playlists)
    if play:
        open_iina()

if __name__ == "__main__":
    args = sys.argv[1:]
    rooms = set()

    # open local list
    if len(args) < 2:
        platform = ''
        if len(args) == 1:
            platform = args[0]
        if platform == 'd':
            # open directly
            open_iina()
        else:
            local_rooms = get_room_ids(platform=platform)
            rooms.update(local_rooms)
            update_play_list(rooms, play=True)

    # open room by id
    if len(args) == 2:
        platform = args[-2]
        rid = args[-1]
        rooms.add((platform, rid))
        update_play_list(rooms, play=True)


    # add to local
    if len(args) == 3 and args[0] == 'add':
        platform = args[-2]
        rid = args[-1]
        add_room_ids(platform, rid)
        local_rooms = get_room_ids()
        rooms.update(local_rooms)
        update_play_list(rooms)


