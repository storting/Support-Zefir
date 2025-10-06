import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
import datetime
import random
import time
import webbrowser
import subprocess
import wikipedia
from dotenv import load_dotenv
load_dotenv()

# Настройка синтезатора речи
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    """Говорит заданный текст"""
    print("Assistant:", text)
    tts = gTTS(text=text, lang='ru')
    filename = 'temp.mp3'
    tts.save(filename)
    os.system(f'start {filename}')

def listen():
    """Слушает микрофон и возвращает распознанную фразу"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите...")
        audio = r.listen(source)
    
    try:
        command = r.recognize_google(audio, language="ru-RU")
        print("Вы сказали:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Ваш голос не понят.")
        return ""
    except sr.RequestError as e:
        print("Ошибка распознавания:", str(e))
        return ""

def process_command(command):
    if "привет" in command or "здравствуй" in command:
        greetings = ["Привет!", "Здравствуй!", "Рад тебя видеть."]
        response = random.choice(greetings)
    elif "как дела" in command:
        responses = ["Всё отлично, спасибо.", "Нормально, готов помогать вам.", "Хорошо, а у вас как?"]
        response = random.choice(responses)
    elif "текущее время" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        response = f"Сейчас {current_time}."
    elif "открой браузер" in command:
        webbrowser.open_new_tab("https://www.google.com/")
        response = "Открываю браузер."
    elif "найти википедию" in command:
        search_term = command.replace("найти википедию ", "")
        result = wikipedia.summary(search_term, sentences=2)
        response = result
    else:
        response = "Простите, я пока не умею такое делать."
        
    speak(response)

if __name__ == "__main__":
    while True:
        command = listen()
        if command != "":
            process_command(command)
        time.sleep(1)