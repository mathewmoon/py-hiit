import pyttsx3
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep


TP = ThreadPoolExecutor(max_workers=2)


def speak(voice):
    try:
        engine.endLoop()
        del engine
        engine = pyttsx3.init()
    except:
        pass
    #engine = pyttsx3.init()
    engine.setProperty('voice', voice.id)
    engine.say('The quick brown fox jumped over the lazy dog.')
    print(voice.id)
    engine.runAndWait()
    #engine.endLoop()
    #del engine


engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    TP.submit(speak, voice)
    sleep(1)

#tasks = {TP.submit(speak, voice) for voice in voices}

for x in as_completed(tasks):
    try:
        x.result()
    except Exception as e:
        print(e)

sleep(100000)
