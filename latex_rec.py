#!/usr/bin/env python3

import speech_recognition as sr
from os import path
from parse import matrix_parse, process, matrix
import re

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "matrix_test.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    recognized = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + recognized)
    rec_arr = re.findall(r"[\w']+", recognized)
    print("This becomes\n" + matrix(rec_arr, 0 ,len(rec_arr)))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

m_test = """one plus two squared minus root four root times fraction one two denominator three fraction
            matrix element 1 plus 2 element 2 root 4 root element fraction 12 denominator 3 fraction row
            element 2 element 4 element 7 matrix"""
marr = m_test.split()
print(process(marr, 0, len(marr)))
