import time
import speech_recognition as sr
import os
import subprocess
import sys
from pathlib import Path


def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


possible_options = [
    {
        "keywords": ['kargo', 'takip'],
        "file": "audio/kargo_takip.mp3"
    },
    {
        'keywords': ['sipariş', 'durum'],
        "file": "audio/siparis_durumu.mp3"
    },
    {
        'keywords': ['yakın', 'en'],
        "file": "audio/ptt_adres.mp3"
    },
    {
        "keywords": ["deprem", "sigorta"],
        "file": "audio/deprem_sigortası.mp3"
    },
    {
        "keywords": ["kredi", "tüketici"],
        "file": "audio/tüketici_kredisi.mp3"
    }
]

while True:
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Lütfen konuşun")
            audio = recognizer.listen(source, phrase_time_limit=3)
        recognized_speech = recognizer.recognize_wit(audio, '6LVHLSJWLJOJVUZ26ZMXKDY7K26ZQ4DG').lower()

        if not recognized_speech.strip():
            continue

        print("Söylendi: ", recognized_speech)

        for item in recognized_speech.split():
            for option in possible_options:
                if item in option['keywords']:
                    open_file('{}/{}'.format(Path().absolute(), option['file']))
                    time.sleep(6)

    except sr.UnknownValueError:
        print("Konuşma anlaşılamadı. Tekrar deneyin")
    except sr.RequestError as e:
        print("Bağlantı kurulamadı ! {0}".format(e))
