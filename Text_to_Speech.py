from gtts import gTTS #Google Text to Speech API
import os
text = "Hello"
language = 'en' #English
speech = gTTS(text = text, lang = language, slow = False)
speech.save("test.mp3")
os.system("start test.mp3")