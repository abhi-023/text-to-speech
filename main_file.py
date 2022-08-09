# install pyttsx3 is a text-to-speech conversion library in Python.
# type pip install pyttsx3 inside the terminal for installation
import pyttsx3
text_speech = pyttsx3.init()
answer = input("what do you want to convert into speech:")
text_speech.say(answer)
text_speech.runAndWait()

