
from flask import Flask
from pyfcm import FCMNotification
from firebase import Firebase
app = Flask(__name__)

config = {
   "apiKey": "AIzaSyCXPd4UyuKTV2tQmll8tLqr7n4fi63VRXE",
  "authDomain": "php-mbsa.firebaseapp.com",
  "databaseURL": "https://php-mbsa-default-rtdb.firebaseio.com",
  "projectId": "php-mbsa",
  "storageBucket": "php-mbsa.appspot.com",
  "messagingSenderId": "495110636533",
  "appId": "1:495110636533:web:fdf96b5e19d9e73324d6bc",
  "measurementId": "G-YFPZ05BCKE"
}

firebase = Firebase(config)
db = firebase.database()
push_service = FCMNotification(api_key="AAAASNIN9qU:APA91bHwPAZyam3Uc4RZd2abDCeqj8Y8d8z-YR40EbnzaX98242piyWtuNn_WzGG1Rj4YTCid-1hJmtDT2Xle8gku65N32mMHdf5oKFPr6It5_npF7hbV7BzcUZSvEmmkhf-SOVTKQoN")

@app.route("/")
def start():
    def stream_handler(message):
      result = push_service.notify_single_device(registration_id="cRsi5BbdRF-L0iIk4AMOjC:APA91bFUaTUVXmwGlSVgOm8HqLm1c64acOu55NJCR0Cyni3CTn8wXFnwb4A_yKrGUwPhJxak60KnJmPUMXpKadVRgCnefW832XkCpJozw-NvKO4oA_lOC3uj8GEDOLfzGFHtmKIz_Us9", message_title="Data Changed", message_body=message["data"])
    my_stream = db.child("data").stream(stream_handler)
    return "Flask Server Started with all things!!!"




