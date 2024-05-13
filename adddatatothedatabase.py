import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://attendance-major-project-default-rtdb.firebaseio.com/"
    })

ref = db.reference('Students')

data = {
    "2142000286":
    {
        "name": "Vaibhav Chandra" ,
        "major": "BCA",
        "starting_year": 2021,
        "total_attendance": 8,
        "standing": "D",
        "year": 3,
        "last_attendance_time": "2024-05-24",
    }

}

for key,value in data.items():
    ref.child(key).set(value)