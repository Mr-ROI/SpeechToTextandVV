import speech_recognition as sr
import pyaudio
import pyttsx3
import main
import wave
# words = main.repeater()


def speakTest(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


# words = "My name is Bharath, Hello how are you?"
# speakTest(words)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# p = pyaudio.PyAudio()

# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)

# print("* recording")

# frames = []
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)

# print("* done recording")

# stream.stop_stream()
# stream.close()
# p.terminate()

# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()


r = sr.Recognizer()
audio_path = "output.wav"
with sr.AudioFile(audio_path) as source:
    audio_data = r.record(source)

    try:
        text = r.recognize_google(audio_data)
        print(text)
        if "hey roi" in text.lower():
           speakTest("How can i help you?")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")






