import numpy as np
import serial
import joblib
import serial.tools.list_ports
import warnings
from sklearn import metrics
import firebase_admin
import pickle
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.ensemble import RandomForestClassifier
from firebase_admin import credentials, firestore
from firebase_admin import db
# import sklearn
np.seterr(all='ignore')
warnings.filterwarnings("ignore")
with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
# Load your pre-trained machine learning model
# model=joblib.load('model_knn1')
cred = credentials.Certificate('secret key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://hack4tkm-8a06f-default-rtdb.firebaseio.com/"
})

ref = db.reference('Database reference')
ref = db.reference("/")
dbb=firestore.client()

# import json
# with open("data.json", "r") as f:
# 	file_contents = json.load(f)
# ref.set(file_contents)
# print(ref.get())


# Assuming 'model' is your trained RandomForestRegressor model
# Save the model to a pickle file

# Later, you can load the model back using:
# with open('model1.pkl', 'rb') as f:
#     model = pickle.load(f)
# Load model architecture from JSON
from keras.models import model_from_json
with open('milk_model2.json', 'r') as json_file:
    loaded_model_json = json_file.read()

# Create model
loaded_model = model_from_json(loaded_model_json)

# Load weights into new model
loaded_model.load_weights("model1.h5")
# import joblib
# model=joblib.load('knn')

# Initialize variables
# model=joblib.load('random_forest_model.pkl')
data_list = []
value_count = 0
values_per_sample = 11  # Adjust as needed
cnt=0
# Function to process and predict based on incoming data
def process_and_predict(data):
    global cnt

    global data_list, value_count
    
    try:   
        # Convert the received data into an integer
        values=[int(value) for value in data.split(',')]
        import random
        
        if (len(values) == 11):
            dic = {
            "1":values[0],
            "2":values[1],
            "3":values[2],
            "4":values[3],
            "5":values[4],
            "6":values[5],
            "7":values[6],
            "8":values[7],
            "9":values[8],
            "10":values[9],
            "11":values[10]
        }
            array=np.array(values)

            array=np.expand_dims(array,axis=0)
            # print(array)
            y_pred=loaded_model.predict(array)
            final=y_pred[0][0]*10
            final+=random.randint(-1,1)
            # print(y_pred)
            # ans=loaded_model.predict([[597,414,500,403,552,323,305,305,274,247,253]])
            # print(ans)
            
            data={
                "values":dic,
                "pred":int(final)
            }
            print(values)
            dbb.collection("Shelf1").document(f"T{cnt}").set(data)
            dbb.collection("Shelf1").document("Tfinal").set(data)
            cnt+=1
        else:
            print("Value Error")

    except ValueError:
        print("Received data is not an integer:")

# Find and open the Arduino serial port
def find_serial_port():
    ports = serial.tools.list_ports.comports()
    arduino_port = None
    for port in ports:
        if "COM3" in port.device:  # Adjust this based on your Arduino's device name
            arduino_port = port.device
            break
    return arduino_port

arduino_port = find_serial_port()
if arduino_port:
    ser = serial.Serial(arduino_port, baudrate=9600, timeout=1)
    
    while True:
        data = ser.readline().decode().split('\r\n')[0]
        process_and_predict(data)
else:
    print("Arduino port not found.")
