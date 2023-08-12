import random

import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
from config import mykey
import time
chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = mykey
    chatStr += f"Bhagat: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
def ai(prompt):
    openai.api_key = mykey
    text=f"OpenAi response for Prompt : {prompt} \n*****************\n"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    print(response["choices"][0]['text'])
    text+= response["choices"][0]['text']
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('jarvis')[1:]).strip()}.txt",'w') as f:
        f.write(text)


def say(text):
    engine = pyttsx3.init()
    engine.setProperty('languages', 'hi')
    engine.say(text)
    engine.runAndWait()

def stop_speaking():
    engine.stop()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language="en-in")
            print(f"User said:{query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry"

if __name__ == '__main__':
    musicPath = r"C:\Users\kumar\PycharmProjects\kalki\intro.mp3"
    os.system(f"start  {musicPath}")
    time.sleep(5.5)
    # say("Hello I am Lord     Kkaallkii")
    while True:
        print("Listing...")
        say("btao kis tarah sahaytha karu")
        query=takeCommand()
        sites=[["youtube","https://www.youtube.com"],["wikipedia","https://wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir")
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            os.system(f"open {musicPath}")

        elif "the time" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")

        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")

        elif "open pass".lower() in query.lower():
            os.system(f"open /Applications/Passky.app")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
            if "stop" in query.lower():
                stop_speaking()

