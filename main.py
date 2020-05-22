import sys
from GetUrl import GetUrl


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

    get_real_url_by_platform(platform, rid)
