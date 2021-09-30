from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
socketio = SocketIO(app)

#defines the job
def job():
    new_price = random.random();
    #job emits on websocket
    socketio.emit('price update',new_price, broadcast=True)

#schedule job
scheduler = BackgroundScheduler()
running_job = scheduler.add_job(job, 'interval', seconds=4, max_instances=1)
scheduler.start()

@app.route('/')
def index():
    return render_template('index.html')

