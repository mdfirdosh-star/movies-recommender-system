import requests
import json
r=requests.post("https://github.com/mdfirdosh-star/mdfirdosh-star")
print(r.status_code) 
print(r.json())
