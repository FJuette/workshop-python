import requests as r
import re

def make_w_req(url):
    response = r.get(url)
    return str(response.content)


def find_urls(content):
    m = re.findall('href=[\'"]?([^\'" >]+)', content)
    print(m)


f = open("links.txt", mode="r")
lines = f.readlines()
for l in lines:
    c = make_w_req(l.replace("\n", ""))
    find_urls(c)
f.close()
