from gtts import gTTS #Google Text to Speech API
import OS
text = "My name is Ritesh Prasad Singh"
language = 'en' #English
speech = gTTS(text = text, lang = language, slow = False)
speech.save("test.mp3")
os.system("start test.mp3")