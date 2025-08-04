import speech_recognition as sr
import pyaudio as pya


def main():
    
    r  =  sr.Recognizer()

    with sr.Microphone() as source:
        print("talk")
        audio_text  = r.listen(source)
        print("times up")
    
    try:
        print("Text: "+r.recognize_google(audio_text))
        return r.recognize_google(audio_text)
    except:
         print("Sorry, I did not get that")

if __name__ == "__main__":
    main()
