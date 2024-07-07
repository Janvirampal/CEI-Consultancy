import json
import requests
url="http://api.open-notify.org/iss-now.json"
headers={

 "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"

}
response=requests.get(url,headers=headers)
print(response)
print(response.text)