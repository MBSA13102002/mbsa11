from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
from pyfcm import FCMNotification
push_service = FCMNotification(api_key="AAAASNIN9qU:APA91bHwPAZyam3Uc4RZd2abDCeqj8Y8d8z-YR40EbnzaX98242piyWtuNn_WzGG1Rj4YTCid-1hJmtDT2Xle8gku65N32mMHdf5oKFPr6It5_npF7hbV7BzcUZSvEmmkhf-SOVTKQoN")
from firebase import Firebase
config = {
    "apiKey": "AIzaSyBQUpIYvs0WKfP5IMD4TE2IWTvpb5U34Cc",
   "authDomain": "portfoliomanagement-16f09.firebaseapp.com",
    "databaseURL": "https://portfoliomanagement-16f09.firebaseio.com",
    "projectId": "portfoliomanagement-16f09",
    "storageBucket": "portfoliomanagement-16f09.appspot.com",
    "messagingSenderId": "505793158040",
    "appId": "1:505793158040:web:14b9466a349235ef8b69ed",
    "measurementId": "G-MRCWJ4R5RJ"
}
firebase = Firebase(config)
db = firebase.database()

app = Flask(__name__)
socketio = SocketIO(app)
def stream_handler(message):
    __name = db.child("stream").child("name").get().val()
    socketio.emit('price update',__name, broadcast=True)
    result = push_service.notify_single_device(registration_id="cRsi5BbdRF-L0iIk4AMOjC:APA91bFUaTUVXmwGlSVgOm8HqLm1c64acOu55NJCR0Cyni3CTn8wXFnwb4A_yKrGUwPhJxak60KnJmPUMXpKadVRgCnefW832XkCpJozw-NvKO4oA_lOC3uj8GEDOLfzGFHtmKIz_Us9", message_title="Changed", message_body=__name)


my_stream = db.child("stream").stream(stream_handler)
@app.route('/')
def index():
    __name = db.child("stream").child("name").get().val()
    socketio.emit('price update',__name, broadcast=True)
    return render_template('index.html')

