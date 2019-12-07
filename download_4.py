import requests as r
import re

def make_w_req(url):
    response = r.get(url)
    return str(response.content)


def find_urls(content):
    return re.findall('href=[\'"]?([^\'" >]+)', content)


def write_urls(urls):
    with open("found_4.txt", "a+") as f:
        for url in urls:
            f.write(url + "\n")


f = open("links.txt", mode="r")
lines = f.readlines()
f.close()
for l in lines:
    c = make_w_req(l.replace("\n", ""))
    urls = find_urls(c)
    write_urls(urls)
