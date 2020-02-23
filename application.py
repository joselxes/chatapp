import os
import requests
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
def call(new):
    newnew=""
    for i in range (0,len(new)-1):
        if (new[i]==" " and new[i+1]==" "):
            newnew=newnew
        else:
            newnew=newnew+new[i]
    if (new[-1]!=" "):
        newnew=newnew+new[-1]
    if (newnew[0]==" "):
        newnew=newnew[1 : : ]
    return newnew

def soloCanal(soloCanales):
  salasChat=[]
  for i in soloCanales:
    salasChat.append(i["canal"])
  return salasChat

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
channels=[]
channelsA=[]
channelsA.append({"canal":"jose","chat":["jajaja","jijiji"],"usuarios":[]})
channels.append("jose")
mensajes=["jajaj"]
@app.route("/")
def index():
    return render_template("start.html")
    # return render_template("createRoom.html",nName="jose",channels=channels)

@app.route("/newChannels",methods=["POST"])
def newChannels():
    newChannel = call(request.form.get("newChannel"))
    userName = request.form.get("username")
    for k in channelsA:
        if newChannel == k["canal"]:
            print(k["canal"],k["chat"])
            return jsonify({"success":False,"newChannel":channels})

    channelsA.append({"canal":newChannel,"chat":[],"usuarios":[]})
    channels.append(newChannel)
    print(channelsA[-1]["canal"],channelsA[-1]["chat"])
    return jsonify({"success":True,"newChannel":channelsA[-1]["canal"]})

    # if (newChannel in channels):
    #     return jsonify({"success":False,"newChannel":channels})
    # else:
    #     channels.append(newChannel)
    #     return jsonify({"success":True,"newChannel":channels[-1]})

@app.route("/chatList",methods=["POST"])
def chatList():
     if request.method == "POST":
        nickName=request.form.get("nickName")
        return render_template("createRoom.html",nName=nickName,channels=soloCanal(channelsA))
     return "error"

@app.route("/chatList/<Source>", methods=["GET","POST"] )
def bookdata(Source):
    # return jsonify({"success":True,"Source":Source})
    userName=request.form.get("userName")
    for k in channelsA:
        if Source == k["canal"]:
            print("::::::::::::::::::::::::::::::::::")
            print(userName)

            return render_template("index.html",mensajes=k["chat"],source=Source,userName=userName)

@socketio.on("submit mensaje")
def vote(data):
    contenido = data["contenido"]
    roomName = data["nombreCanal"]
    userName=data["userName"]
    print("---------------------------------------------")
    print({"contenido": contenido,"roomName":roomName,"userName":userName})
    for k in channelsA:
        if roomName == k["canal"]:
            k["chat"].append(contenido)
            k["usuarios"].append(userName)
    # mensajes.append(contenido)
    emit("announce mensaje", {"contenido": contenido,"roomName":roomName,"userName":userName}, broadcast=True)





# if __name__ == "__main__":
#     socketio.run(app)
