from flask import Flask, render_template
from flask_socketio import SocketIO,emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def connect():
    with open("/home/zejie123/webapp/toilet_app/static/lol.txt","r") as f:
        data_list = f.readlines()
        data = data_list[-1]
    emit("data",data)

@socketio.on("sender")
def sender():
    with open("/home/zejie123/webapp/toilet_app/static/lol.txt","r") as f:
        data_list = f.readlines()
        data = data_list[-1]
    emit("data",data)

if __name__ == "__main__":
    socketio.run(app)