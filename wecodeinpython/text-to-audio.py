#pip install gtts
from gtts import gTTS

#pip install playsound
from playsound import playsound

audio = 'speech.mp3'
language = 'en'
sp = gTTS(text = "Writing your text to convert: ",
            lang = language, slow = False)

sp.save(audio)
playsound(audio)