import requests
import cv2 as cv
import numpy as np

# select image
img = "./austin10_250.tif"
data = open(img, 'rb').read() # bytes

files = {'image': ('test.jpg', data, bytes)}

url = "http://0.0.0.0:5000/" + "api/test"

content_type = "api/test"
headers = {'content-type': content_type}

r = requests.post(url, files=files, headers=headers)

print(r.content)
