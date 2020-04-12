from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
socketio = SocketIO(app)

# using a decorator here, listening for message event
@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)

    # send out msg to everyone on server
    # broadcast defaults to send msg to client you received a msg from
    # can break this into namespaces, and rooms; check into this later
    send(msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')