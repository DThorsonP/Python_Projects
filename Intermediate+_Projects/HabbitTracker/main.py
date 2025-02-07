import requests

# My first graph, woo!
# https://pixe.la/v1/users/dthorson2700/graphs/graph1.html

USERNAME = "dthorson2700"
TOKEN = "Y`=(-Ay[MS+0p7.r6AuQ*o=;VBU-c15,T++$IW0^~i)H"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "sora", # sora == blue
}

headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)


# date format yyyyMMdd

