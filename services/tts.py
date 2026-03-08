from gtts import gTTS
import os

def speak(text):

    tts = gTTS(text=text, lang="en")

    file = "response.mp3"

    tts.save(file)

    print("Voice response saved:", file)

    os.system("start response.mp3")