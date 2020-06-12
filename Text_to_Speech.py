from gtts import gTTS #Google Text to Speech API
import os
text = "Hi, I am your assistance. How can I help you"
language = 'en' #English
speech = gTTS(text = text, lang = language, slow = False)
speech.save("test.mp3")
os.system("start test.mp3")