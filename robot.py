from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
perf_counter(time)
from tkinter import*

bot=ChatBot("bot")
convo=["hello,"
       "hi there !"
       "what is your name ?"
       "My name is  BOT and i'm created by Saurabh"
       "How are you ?"
       "i'm fine !what about you ?"
       "In which city you live"
       "I live in Gurgaon"
       "In which langauge you talk"
       "I mostly talk in English"

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
def ask_from_bot():
    query=textF.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert("END","you:"+query)
    msgs.insert(END,"bot:",+str(answer_from_bot))
    textF.delete(0,END)
main=Tk()
main.geometry("500x550")
main.title("My chat bot")
img=PhotoImage(file='rbt.gif')
photoL=Label(main,image=img)
photoL.pack(pady=5)
frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=10)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
#creating text field
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="Ask from bot",font=("Verdana,20"),command=ask_from_bot)
btn.pack()
main.mainloop()
