import requests as r
import re

def make_w_req(url):
    response = r.get(url)
    return str(response.content)


def find_urls(content):
    return re.findall('href=[\'"]?([^\'" >]+)', content)


def write_urls(urls):
    with open("found_5.txt", "a+") as f:
        for url in urls:
            f.write(url + "\n")


def filter_url(url):
    if str(url).startswith("http"):
        return True
    return False


def remove_trailing_char(url):
    if str(url).endswith("/"):
        return url[0:len(url) - 1]
    return url


f = open("links.txt", mode="r")
lines = f.readlines()
f.close()
for l in lines:
    c = make_w_req(l.replace("\n", ""))
    urls = find_urls(c)
    urls = filter(filter_url, urls)
    urls = list(map(remove_trailing_char, urls))
    urls = list(dict.fromkeys(urls))
    write_urls(urls)
