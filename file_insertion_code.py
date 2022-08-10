fh=open("main.py","r")
myText=fh.read()
import pyttsx3
text_speech = pyttsx3.init()
text_speech.say(myText)
text_speech.runAndWait()