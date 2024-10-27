import queue
import pyttsx3
import time

def voice(speech_q):

    while True:
        result = speech_q.get()
        print("Consumer received:", result)
        engine = pyttsx3.init()
        engine.setProperty('rate', 50)
        engine.say(result)
        engine.runAndWait()
