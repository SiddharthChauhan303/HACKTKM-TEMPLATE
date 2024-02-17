# import pyrebase

# # from collections.abc import MutableMapping  # Importing MutableMapping from collections.abc
# import firebase_admin


# config ={
#     "apiKey": "AIzaSyB13KOx1Xjf8rfHpKPZziN9w8WxI0nH2XI",
#     "authDomain": "hack4tkm-8a06f.firebaseapp.com",
#     "databaseURL": "https://hack4tkm-8a06f-default-rtdb.firebaseio.com",
#     "projectId": "hack4tkm-8a06f",
#     "databaseURL": "https://hack4tkm-8a06f-default-rtdb.firebaseio.com/",
#     "storageBucket": "hack4tkm-8a06f.appspot.com",
#     "messagingSenderId": "1059856717453",
#     "appId": "1:1059856717453:web:0a5261d4e6c9d4455db4c4",
#     "measurementId": "G-J6G8HNRSMB"
# }
# cred_obj = firebase_admin.credentials.Certificate('....path to file')
# default_app = firebase_admin.initialize_app(cred_object, {
# 	'databaseURL':databaseURL
# 	})
# firebase = pyrebase.initialize_app(config)
# database = firebase.database()

# data = {"Age": 20, "Name":"Kushal"}

# database.push(data)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('secret key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://hack4tkm-8a06f-default-rtdb.firebaseio.com/"
})

ref = db.reference('Database reference')
ref = db.reference("/")
import json
with open("data.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)
print(ref.get())