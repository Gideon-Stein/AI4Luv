import queue
import pyttsx3
import time

def voice(speech_q):
    engine = pyttsx3.init()
    engine.setProperty('rate', 90)
    engine.setProperty('voice', 'english_rp+f4+1')
    while True:
        result = speech_q.get()
        print("Line recieved:", result)
        engine.say(result)
        engine.runAndWait()