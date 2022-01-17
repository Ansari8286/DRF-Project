import requests
import json
# r = requests.get(url = "http://127.0.0.1:8000/personView/")

# data = r.json()

# print(data)

data = {
    'name': 'Amjad Ansari 1234', 
    'address': 'koliwada plot', 
    'city': 'mumabi', 
    'state': 'maharashtra', 
    'country': 'india', 
    'pincode': '400060', 
    'phone_number': '8888888888', 
    'email': 'Ansari.amjad8286@gmail.com'
}

json_data = json.dumps(data)
print(json_data)
r = requests.post(url = "http://127.0.0.1:8000/personView/", data=json_data)
data = r.json()
print(data)