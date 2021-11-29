import Tkinter as tk
from gtts import gTTS
from playsound import playsound

win = tk.Tk()
win.title("TEXT TO SPEECH")
win.geometry("350x100")

#Function Speech
def text_to_speech():
    text = entry.get()
    speech = gTTS(text=text,lang="en")
    speech.save("r'\Desktop\hello.mp3")
    playsound("r'\Desktop\hello.mp3")

#Create Label
label = tk.Label(win,text="Enter Here :")
label.grid(row=0,column=0)

#Entry Point
entry = tk.Entry(win)
entry.grid(row=1,column=0)

#Create Button
button = tk.Button(win,text="Go",command=text_to_speech)
button.grid(row=1,column=1)

win.mainloop()
