import speech_recognition as sr

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # listen for 1 second and create the ambient noise energy level
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=5)
