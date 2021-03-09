import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "khaleel20"
username = "khaleel"
user_params = {
    "token": TOKEN,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
Graph1 = "graph1"
graph_config = {
    "id": Graph1,
    "name": "Coding Practice",
    "unit": "hr",
    "type": "float",
    "color": "ajisai"
}
header = {
    "X-USER-TOKEN": TOKEN
}
today = datetime.now()
response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
print(response.text)

get_endpoint = f"{pixela_endpoint}/{username}/graphs/{Graph1}"
g_header = {
    "X-USER-TOKEN":TOKEN
}
today =today.strftime("%Y%m%d")
pixel_data = {
    "date": "20210308",
    "quantity": "5.3"
}
response = requests.post(url=get_endpoint, json=pixel_data, headers=header)
print(response.text)

put_endpoint = f"{pixela_endpoint}/{username}/graphs/{Graph1}"
print(put_endpoint)
change_data = {
    "date": today,
    "quantity": "5.4"
}
response = requests.post(url=put_endpoint, json=change_data, headers=header)
print(response.text)
delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{Graph1}/20210308"
response = requests.delete(url=delete_endpoint, headers=header)