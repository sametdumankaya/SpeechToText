import speech_recognition as sr

audio_file = 'ses.wav'
r = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)

try:
    print(r.recognize_wit(audio, '6LVHLSJWLJOJVUZ26ZMXKDY7K26ZQ4DG'))
except sr.UnknownValueError:
    print("Anlaşılamadı !")
except sr.RequestError as e:
    print("Bağlantı kurulamadı. {}".format(e))