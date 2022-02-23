# this file sends image.jpg to gcp
import os
import base64
import json
import urllib
import requests
with open("image.jpg","rb") as image_file:
	image_read = base64.b64encode(image_file.read()).decode("utf-8")
	#print(image_read)
	body = {
"user_id":"jisoo","camera_id":"camera1","set_id":"set1","image":image_read}
	url = "http://35.219.175.143:5000/upload"
	url = "http://192.168.2.242:5001/upload"
	headers = {'Content-Type':'application/json'}
	response = requests.post(url,data = json.dumps(body), headers=headers)
	#print(image_read)
