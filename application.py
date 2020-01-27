import os
import requests
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
rooms=[]

@app.route("/")
def index():
    return render_template("start.html")

@app.route("/addRoom",methods=["POST"])
def convert():
    newRoom = request.form.get("newRoom")
    if (newRoom in rooms):
        return jsonify({"success":False})
    rooms.append({newRoom})
    return jsonify({"success":True,"rooms":rooms})

@app.route("/chatList",methods=["POST"])
def chatList():
    # if request.method == "POST":
        nickName=request.form.get("nickName")
        return render_template("createRoom.html",nName=nickName)
    # return "error"

@socketio.on("submit mensaje")
def mensaje(data):
    selection = data["mss"]
    emit("announce mensaje",{"mss":selection},broadcast=True)


if __name__ == "__main__":
    socketio.run(app)
