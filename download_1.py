import requests as r

response = r.get("https://www.tu-clausthal.de/")
print(response.status_code)
print(response.text)