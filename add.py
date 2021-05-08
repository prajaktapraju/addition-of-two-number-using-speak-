import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
from time import ctime
import gtts
import math
import numpy

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def add():

  r = sr.Recognizer()
  with sr.Microphone() as source:
    speak("Hello")

    speak("enter the first number..")
    num1 =int(input())

    speak("enter the second number..")
    num2 = int(input())

    add = num1 + num2

    speak('the addition of  {} and {} is  {}'.format (num1, num2, add))
    print('the addition of  {} and {} is  {}'.format (num1, num2, add))


if __name__ == "__main__":
    speak("welcome to AI world")
    add()