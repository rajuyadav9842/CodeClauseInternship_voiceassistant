import pyttsx3 as p    # pip install pyttsx3
import speech_recognition as sr     # pip install speech recognition

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',120)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()




r = sr.Recognizer()

speak("hello RAAJU  i'm your voice assistant . how are you?")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("i am  also having good day Raaju ")
speak("what can i do for you sir ?? ")


with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("you need information related which topic Raaju ? ")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening")
        audio = r.listen(source)
        infor = r.recognize_google(audio)


from selenium import webdriver
import time


class infow():
    def _init_(self):
        # Provide the correct path to the ChromeDriver executable
        self.driver = webdriver.Chrome()

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://tinyurl.com/22zcqja3")

        time.sleep(300)

assist = infow()
assist.get_info("chandrayaan-3-vikram-lander")
