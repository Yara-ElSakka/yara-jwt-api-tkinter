# Fetch API Tkinter.
# James Webb Telescope (JWT).
# Yara ElSakka.
# 03.01.22
# code done at the class time.

from tkinter import *
from requests import *
import json

# This is my app to find LIVE information about JWT using Nasa's public JWT API :)
# Since Nasa JWT API is made in json, we need to import json to our code.

jwt_API = get("https://api.jwst-hub.com/track")
jwt_cont= jwt_API.content

# To check what kind of information is avalabile within the API:
# print(jwt_cont)

data = json.loads(jwt_cont)

# Collecting data by assigning it to variables:

data_distanceEarthKm = data ['distanceEarthKm']
data_launchElapsedTime = data ['launchElapsedTime']
data_distanceL2Km = data ['distanceL2Km']
data_percentageCompleted = data ['percentageCompleted']
data_speedKmS = data ['speedKmS']
data_currentDeploymentStep= data ['currentDeploymentStep']

# Now, The Tkinter interface:

programWindow = Tk()
programWindow.title("Tracking JWT App, By Yara")
programWindow.geometry('600x800')
programWindow.resizable(width=1,height=1)
programWindow.configure(bg="#DB6B97")

# Close Button widget :

closeButton = Button(text = "close program", command = programWindow.destroy)
closeButton.pack(pady = 20, side = TOP)

# Live info labels:

liveInfo_01 = Label(text=f"Distance from Earth in (Km) = {data_distanceEarthKm}",bg="#FFF89A")
liveInfo_01.pack(pady=20)

liveInfo_02 = Label(text=f"Launch Elapsed Time (dd:hh:mm:ss) = {data_launchElapsedTime}",bg="#FFF89A")
liveInfo_02.pack(pady=20)

liveInfo_03 = Label(text=f"Percentage of Mission Completed = {data_percentageCompleted} %",bg="#FFF89A")
liveInfo_03.pack(pady=20)

liveInfo_04 = Label(text=f"JWT Speed in Km / S = {data_speedKmS}",bg="#FFF89A")
liveInfo_04.pack(pady=20)

liveInfo_05 = Label(text=f"Current Deployment Step: {data_currentDeploymentStep}",bg="#FFF89A")
liveInfo_05.pack(pady=20)

liveInfo_06 = Label(text=f"distanceL2Km = {data_distanceL2Km}",bg="#FFF89A")
liveInfo_06.pack(pady=20)

# adding a fance image:

img  = PhotoImage(file='/Users/yaraelsakka/PycharmProjects/yara-jwt-api-tkinter/115_new.png')
yara = Label(image = img)
yara.pack(pady = 20, side = BOTTOM)

mainloop()

# end of code.
# 03.01.22