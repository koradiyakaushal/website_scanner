import urllib.request
import io
import certifi


def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + "robots.txt", cafile=certifi.where())
    # req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding='UTF-8')
    return data.read()


# print(get_robots_txt("https://www.youtube.com/"))
