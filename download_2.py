import requests as r
import re


def make_w_req(url):
    response = r.get(url)
    print(response.status_code)
    print(response.text)


f = open("links.txt", mode="r")
lines = f.readlines()
for l in lines:
    make_w_req(l.replace("\n", ""))
f.close()
