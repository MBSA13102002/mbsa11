from flask import Flask ,render_template
from flask_socketio import SocketIO, send,emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + str(msg))
	send(msg, broadcast=True)


# @app.route('/')
# def start():
#     	return render_template('index.html')

