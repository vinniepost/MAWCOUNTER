import speech_recognition as sr
from pydub import AudioSegment

FILE = "test.wav"


r = sr.Recognizer()
with sr.AudioFile('test.wav') as source:
    audio: sr.AudioData = r.record(source)  # read the entire audio file

    print("Transcription: " + r.recognize_google(audio,language = 'nl-BE'))
    f = open("Transcription.txt", "w")
    f.write("Transcription: " + r.recognize_google(audio,language = 'nl-BE'))
    print(f.read())
