
from pickletools import int4
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()


#def speak(text):
#engine.say(text) 
#engine.runAndWait()



r = sr. Recognizer()
with sr.Microphone() as source:

      
    audio = r.listen(source)
    text = r.recognize_google(audio, language = 'en')
    print(text)

voice = text.isnumeric()

engine.say(voice) 
engine.runAndWait()
print(voice)  