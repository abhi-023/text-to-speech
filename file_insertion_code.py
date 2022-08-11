import pyttsx3

try:
    fh = open(input("Specify the path of the file: "), "r")
    myText = fh.read()
    text_speech = pyttsx3.init()
    text_speech.say(myText)
    text_speech.runAndWait()
except FileNotFoundError:
    print('FILE DOES NOT EXISTS IN THE SPECIFIED PATH')


