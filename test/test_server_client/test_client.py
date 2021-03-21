import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 78, "name": "Joe", "views": 1234},
    {"likes": 15, "name": "Tim", "views": 12345},
    {"likes": 69, "name": "Pablo", "views": 69},
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.delete(BASE + "video/0")
print(response)

input()

response = requests.get(BASE + "video/1")
print(response.json())