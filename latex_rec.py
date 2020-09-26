#!/usr/bin/env python3

import speech_recognition as sr
from os import path
from parse import matrix_parse

print("Hello World")
print("pls work")

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "matrix_test.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    recognized = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + recognized)
    print("This becomes\n" + matrix_parse(recognized))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

