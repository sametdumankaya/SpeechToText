import time
import speech_recognition as sr


def callback(recognizer, audio):
    possible_options = [
        {
            "keyword": 'takip',
            "option": "kargo_takip.mp3"
        },
        {
            'keyword': 'sipariş',
            "option": "sipariş_durumu.mp3"
        },
        {
            'keyword': 'en yakın',
            "option": "en_yakın_ptt.mp3"
        },
        {
            "keyword": "deprem sigorta",
            "option": "deprem_sigortası.mp3"
        },
        {
            "keyword": "tüketici kredi",
            "option": "tüketici_kredisi.mp3"
        }
    ]
    try:
        recognized_speech = recognizer.recognize_wit(audio, '6LVHLSJWLJOJVUZ26ZMXKDY7K26ZQ4DG').lower()
        print(recognized_speech)

    except sr.UnknownValueError:
        print("Konuşma anlaşılamadı. Tekrar deneyin")
    except sr.RequestError as e:
        print("Bağlantı kurulamadı ! {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)

for _ in range(50):
    time.sleep(0.1)

stop_listening(wait_for_stop=False)

while True:
    time.sleep(0.1)
