import speech_recognition as sr
import pyaudio
import pyttsx3
import main

words = main.main()

def speakTest(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

speakTest(words)