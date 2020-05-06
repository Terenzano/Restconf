import requests
from pprint import pprint

router = {"ip": "10.10.20.181", "port": "443", "user": "cisco", "password": "cisco"
          }

url = "https://10.10.20.181:443/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet2"

headers = {
    'Content-Type': "application/yang-data+json",
    'Accept': "application/yang-data+json",
    'Authorization': "Basic dmFncmFudDp2YWdyYW50,Basic Y2lzY286Y2lzY28=",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Cache-Control': "no-cache",
    'Postman-Token': "164f93b3-3fa3-4ca0-bee3-3c7093f827e8,c19c9a50-2157-4cda-8dc2-4293fd784767",
    'Host': "10.10.20.181:443",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.get(url, headers=headers, auth=(
    router['user'], router['password']), verify=False)

api_data = response.json()
pprint(api_data)
print("/" * 50)
pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
print("/" * 50)
if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == 'if-state-up':
    print("Interface is UP!")

