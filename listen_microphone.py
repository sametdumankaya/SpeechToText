import speech_recognition as sr

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=3)
        recognized_speech = r.recognize_wit(audio, '6LVHLSJWLJOJVUZ26ZMXKDY7K26ZQ4DG').lower()
        print(recognized_speech)