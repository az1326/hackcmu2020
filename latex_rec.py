#!/usr/bin/env python3

import speech_recognition as sr
from os import path
from parse import process
import re

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "matrix_test.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)
# print("Working...")

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    recognized = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + recognized)
    rec_arr = recognized.split()
    print("This becomes\n" + process(rec_arr, 0 ,len(rec_arr)))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# s_test = """less than or equal to less than divided by divided"""
# sarr = s_test.split()
# print(process(sarr, 0, len(sarr)))

# m_test = """one plus two squared minus root four close times fraction one two denominator three fraction
#             matrix element 1 plus 2 element 2 root 4 close element fraction 12 denominator 3 fraction row
#             element 2 element 4 element 7 matrix"""
# marr = m_test.split()
# print(process(marr, 0, len(marr)))
