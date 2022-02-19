from urllib import response
import requests
response = requests.get("https://developers.google.com/maps")
print(response.status_code)
# 200 means we are good to go. this was a demo
