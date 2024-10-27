import os
import sys
import wave
import json
import pyaudio
from vosk import Model, KaldiRecognizer


def brain(ear_q, speech_q,generate_q):
    # Path to your model directory

    # Load the Vosk model

    while True:
        result = ear_q.get()
        print("Response prepared")
        if "timmy" in result:
            print("Response prepared")
            speech_q.put("What do you want master. I am your honorable slave." )
        else:
            speech_q.put(result + ", you idiot.")
