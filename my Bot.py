from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from time import perf_counter
from tkinter import*
import pyttsx3 as pp
import speech_recognition as s
import threading

engine=pp.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
print(voices)
def speak(word):
    engine.say(word)
    engine.runAndWait()

bot=ChatBot("bot")
convo=[
    'hi',
    'hi there !',
    'what is your name ?',
    'My name is  BOT and i am created by Saurabh',
    'How are you ?',
    'i am fine, and doing great these days,thank you',
    'In which city you live ?',
    'I live in Gurgaon',
    'In which langauge you talk ?',
    'I usually talk in English',
    'Tell me about your hobbies ?',
    'i am BoT based on a machine learning & and loves to do work',
    'nice talk to you,ok bye bot',
    'bye ! good day'
    ]
trainer=ListTrainer(bot)
trainer.train(convo)
print("Talk to Bot")
#while True:
    #query=input()
    #if query=='exist':
        #break
    #answer=bot.get_response(query)

    #print("Bot :",answer)

def take_query():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("Your bot is listening try to speak")
    with s.Microphone() as m:
       try:
           audio = sr.listen(m)
           query = sr.recognize_google(audio, language='eng-in')
           print(query)
           textF.delete(0, END)
           textF.insert(0, query)
           ask_from_bot()
       except Exception as e :
           print(e)
           print("not recognized")
def ask_from_bot():
    query=textF.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert(END,"you:"+query)
    speak(answer_from_bot)
    msgs.insert(END,"bot:"+str(answer_from_bot))
    textF.delete(0,END)
    msgs.yview(END)
main=Tk()
main.geometry("500x550")


main.title("My chat bot")
img=PhotoImage(file='rbt.gif')
photoL=Label(main,image=img)
photoL.pack(pady=5)
frame=Frame(main)

sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=10,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
#creating text field
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="Ask from bot",font=("Verdana,20"),command=ask_from_bot)
btn.pack()
def enter_function(event):
    btn.invoke()

main.bind('<Return>',enter_function)

def repeatL():
    while True:
        take_query()
t=threading.Thread(target=repeatL)
t.start()
main.mainloop()
########################################################################################################################################################################
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from time import perf_counter
from tkinter import*
import pyttsx3 as pp
import speech_recognition as s
import threading
import webbrowser
import datetime
import wikipedia
import os

engine=pp.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
print(voices)
def speak(word):
    engine.say(word)
    engine.runAndWait()

bot=ChatBot("bot")
bot.storage.drop()
convo=[
    'hi',
    'hi there !',
    'what is your name ?',
    'My name is  BOT and i am created by Saurabh',
    'How are you ?',
    'i am fine, and doing great these days,thank you',
    'In which city you live ?',
    "currently i'm in Gurugram",
    'In which language you talk ?',
    'I usually talk in English',
    'Tell me about your hobbies ?',
    'i am BoT based on a machine learning & and loves to do work',
    'ok bye bot',
    'bye ! good day',
    'what is your age ?',
    'age is for humans and i am machine.'
    'In machines so many functionality is added day by day or some function may obsolete or delete by time',
     ]
trainer=ListTrainer(bot)
trainer.train(convo)
print("Talk to Bot")
#while True:
    #query=input()
    #if query=='exist':
        #break
    #answer=bot.get_response(query)

    #print("Bot :",answer)
def greet():
    currentH=int(datetime.datetime.now().hour)
    if currentH>=0 and currentH<12:
        msgs.insert(END,'Good morning!')
        speak('Good morning !')
    if currentH>=12 and currentH<18:
        msgs.insert(END,'Good Afternoon !')
        speak('Good Afternoon !')
    if currentH>=18 and currentH !=0:
        msgs.insert(END,'Good Evening !')
        speak('Good Evening !')
    ok = "bot: hey i'm your aasistant, how may i help you"
    msgs.insert(END, "bot:" + ok)
    speak("hey i'm your aasistant, how may i help you")

def take_query():

    sr=s.Recognizer()
    sr.pause_threshold=1
    print("Your bot is listening try to speak")
    with s.Microphone() as m:
       try:
           audio = sr.listen(m)
           query = sr.recognize_google(audio, language='eng-in')
           print(query)
           textF.delete(0, END)
           textF.insert(0, query)
           ask_from_bot()
       except Exception as e:
           print(e)
           print("not recognized")

def command():
     query=textF.get()
     if 'open Google' in query:
         speak("okay")
         msgs.insert(END,"you:"+query)
         msgs.insert(END,"bot:okay")
         webbrowser.open('www.google.co.in')
         textF.delete(0, END)
         msgs.yview(END)
     elif'open YouTube' in query:
            okay='okay'
            speak('okay')
            msgs.insert(END,"you:"+query)
            msgs.insert(END, "bot:" + okay)
            webbrowser.open('www.youtube.co.in')
            textF.delete(0, END)
            msgs.yview(END)
     elif'open Gmail'in query:
            okay='okay'
            msgs.insert(END, "you:" + query)
            msgs.insert(END, "bot:" + okay)
            speak('okay')
            webbrowser.open('www.gmail.co.in')
            textF.delete(0, END)
            msgs.yview(END)
     elif 'open map' in query:
         okay = 'okay'
         msgs.insert(END, "you:" + query)
         msgs.insert(END, "bot:" + okay)
         speak('okay')
         webbrowser.open('google map.com')
         textF.delete(0, END)
         msgs.yview(END)
     elif'open Facebook'in query:
         okay = 'okay'
         msgs.insert(END, "you:" + query)
         msgs.insert(END, "bot:" + okay)
         speak('okay')
         webbrowser.open('facebook.com.')
         textF.delete(0, END)
         msgs.yview(END)
     elif 'open stack overflow'in query:
         okay = 'okay'
         msgs.insert(END, "you:" + query)
         msgs.insert(END, "bot:" + okay)
         speak('okay')
         webbrowser.open('stackoverflow.com')
         textF.delete(0, END)
         msgs.yview(END)
     elif 'time' in query:
         strTime=datetime.datetime.now().strftime("%H:%M:%S")
         msgs.insert(END,"bot:The time is "+str(strTime))
         speak(f"the time is {strTime}")
         textF.delete(0, END)
         msgs.yview(END)
     elif 'Wikipedia' in query:
         msgs.insert(END, "you:" + query)
         msgs.insert(END, "bot:searching wikipedia...")
         speak("searching wikipedia....")
         query = query.replace("wikipedia"," ")
         results = wikipedia.summary(query,sentences=1)
         msgs.insert(END, "bot:According to wikipedia")
         msgs.insert(END,"bot:"+str(results))
         speak("According to wikipedia")
         speak(results)
         textF.delete(0,END)
         msgs.yview(END)
     elif 'open word' in query:
         msgs.insert(END, "you:" + query)
         msgs.insert(END, "bot:okay")
         speak("okay")
         path="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
         os.startfile(path)
         textF.delete(0, END)
         msgs.yview(END)

def ask_from_bot():
    query=textF.get()
    if 'open Google'in query:
          command()
    elif 'open YouTube'in query:
         command()
    elif 'open Gmail'in query:
        command()
    elif 'open map' in query:
        command()
    elif 'open facebook' in query:
        command()
    elif'open stack overflow' in query:
        command()
    elif 'time'in query:
        command()
    elif 'Wikipedia' in query:
        command()
    elif 'open word' in query:
        command()
    else:
       answer_from_bot=bot.get_response(query)
       msgs.insert(END,"you:"+query)
       speak(answer_from_bot)
       msgs.insert(END,"bot:"+str(answer_from_bot))
       textF.delete(0,END)
       msgs.yview(END)
main=Tk()
main.geometry("600x550")


main.title("My chat bot")
img=PhotoImage(file='rbt.gif')
photoL=Label(main,image=img)
photoL.pack(pady=5)
frame=Frame(main)

sc=Scrollbar(frame)
msgs=Listbox(frame,width=500,height=10,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
#creating text field
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="Ask from bot",font=("Verdana,20"),command=ask_from_bot)
btn.pack()
def enter_function(event):
    btn.invoke()

main.bind('<Return>',enter_function)

def repeatL():
    greet()
    while True:
        take_query()
t=threading.Thread(target=repeatL)
t.start()
main.mainloop()
