import os
import eel
from engine.features import *
from engine.command import *
from engine.auth import recoganize
eel.init("www")
playAssistantSound()
@eel.expose
def init():
    speak("Ready for face Authentication")
    flag = recoganize.AuthenticateFace()
    if flag == 1:
        speak("Face Authentication Successful")
    else:
        speak("Face Authentication Failed")

speak("Ready for Voice Authentication")
flag = authenticate()
if flag == 1:
    speak("Voice Authentication Successful")
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', block=True)
else:
    speak("Voice Authentication Failed")        

