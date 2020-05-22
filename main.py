import sys
import requests
import subprocess
from GetUrl import GetUrl


def get_room_info(id):
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


def get_room_list(platform, list):
    rooms = []
    room_name = platform
    owner_name = ''
    for id in list:
        url = get_real_url_by_platform(platform, id)
        if url is None:
            continue
        if platform == "douyu":
            room_name, owner_name = get_room_info(id)
        rooms.append({"name": owner_name+"_"+room_name, "url": url})
    return rooms


def generate_play_list(rooms):
    file = "playlist.m3u8"
    with open(file, "a") as f:
        f.seek(0)
        f.truncate()
        for room in rooms:
            info = "#EXTINF:-1,{}\n".format(room["name"])
            f.write(info)
            url = room["url"] + "\n"
            f.write(url)

    f.close()
    subprocess.call(["open", file])


def get_real_url_by_platform(platform, rid):
    get_url_funcs = GetUrl()
    get_real_url = getattr(get_url_funcs, platform)
    url = get_real_url(rid)
    print("Get url succeed:", url)
    return url


if __name__ == "__main__":
    args = sys.argv[1:]
    platform = args[0]
    rid = args[1]
    print(platform, rid)

    playlists = get_room_list(platform, [rid])
    generate_play_list(playlists)
