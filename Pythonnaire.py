import json
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import random


with open('data.json', encoding="utf8") as f:
    data = json.load(f)


questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [0,3,3,1,0,0,3,0,1,1,3,0,0,2,3,2,2,3,2,0] 

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 10):
        x = random.randint(0,19)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "blue",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Bebas Neue",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if score >= 80:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text=f"Excellent !!! Your Score is : {score}/100",background = "#ffffff",
        foreground="green",font = ("Autography",24,"bold"),)
    elif (score >= 50 and score < 80):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text=f"You Can Be Better !!! Your Score is : {score}/100",background = "#ffffff",
        foreground="#FFD43B",font = ("Autography",24,"bold"),)
    else:
        img = PhotoImage(file="bad.png")
        labelimage.image = img
        labelimage.configure(image=img)
        labelresulttext.configure(text=f"You Should Work Hard !!! Your Score is : {score}/100",background = "#ffffff",
        foreground="Red",font = ("Autography",24,"bold"),)


def calc():
    global indexes,user_answer,answers
    x = 0
    global score
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 10
        x += 1
    # print(score)
    showresult(score)


ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 10:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()
    




def startquiz():
    global lblQuestion,r1,r2,r3,r4
    labeltext = Label(
    root,
    text = "Pythonnaire",
    font = ("Autography",25,"bold"),
    background = "#ffffff",
    foreground="#306998"
    )
    labeltext.pack(anchor="w",padx=10)
    
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Bebas Neue", 18),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
        foreground="#306998"
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Bebas Neue", 14),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
        foreground="#FFD43B"
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Bebas Neue", 14),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
        foreground="#FFD43B"
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Bebas Neue", 14),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
        foreground="#FFD43B"
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Bebas Neue", 14),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
        foreground="#FFD43B"
    )
    r4.pack(pady=5)
    lblRules = Label(
    root,
    text = "-> This quiz contains 10 questions\n-> Once you select a radio button that will be your final choice\n-> So, think before you select",
    width = 100,
    font = ("Bebas Neue",14),
    background = "#306998",
    foreground = "#FFD43B",
    )
    lblRules.place(relx = 0.0,
                 rely = 1.0,
                 anchor ='sw')


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()



root = tkinter.Tk()
root.title("PYTHONNAIRE")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)


img1=Image.open("Logo.png")
img1=img1.resize((170,130), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Pythonnaire",
    font = ("Autography",30,"bold"),
    background = "#ffffff",
    foreground="#FFD43B"
)
labeltext.pack(pady=(0,50))


btnStart = Button(
    root,
    text = 'START',
    height = 2, 
    width = 8,
    border = 0,
    background = "#306998",
    foreground = "#FFD43B",
    activebackground="#FFD43B", 
    activeforeground="#306998",
    font = ("Bebas Neue",14),
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    foreground="#306998",
    font = ("Bebas Neue",14),
    justify = "center",
)
lblInstruction.pack(pady=(30,104))

lblRules = Label(
    root,
    text = "-> This quiz contains 10 questions\n-> Once you select a radio button that will be your final choice\n-> So, think before you select",
    width = 100,
    font = ("Bebas Neue",14),
    background = "#306998",
    foreground = "#FFD43B",
)
lblRules.pack()

root.mainloop()