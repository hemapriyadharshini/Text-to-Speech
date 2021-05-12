# import libraries

from tkinter import * #Library for creating GUI interface
from gtts import gTTS #Google Text To Speech
from playsound import playsound #Play sound lib


#Initialize window
root = Tk()
root.geometry('300x300')
root.resizable(0,0)
root.config(bg = 'snow')
root.title('TEXT TO SPEECH')


#Layout- Header and Footer
#Label(root, text = 'Text To Speech' , font='calibri 16 bold' , bg ='white smoke').pack()
Label(root, text ='Copyright © 2021 Hema Sampath. All Rights Reserved.' , font ='calibri 8 bold', bg = 'white smoke').pack(side = BOTTOM)




#Body
Label(root, text ='Enter Text Here', font ='arial 15 bold', bg ='white smoke').place(x=60,y=60)


#text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width ='40')
entry_field.place(x=20 , y=100)


#define function

def Texttospeech():
    Message = entry_field.get() #Get data from text box
    speech = gTTS(text = Message) #Convert text message to speeach
    speech.save('Voice.mp3') #Save message in this sound
    playsound('Voice.mp3')  #Play message in this sound

def Exit():
    root.destroy() #Exit 

def Reset():
    Msg.set("") #Reset

#Button
Button(root, text = 'PLAY',    font = 'arial 12 bold', command = Texttospeech, bg = 'green').place(x=25, y=140)
Button(root,text = 'EXIT',      font = 'arial 12 bold', command = Exit,                bg = 'Red').place(x=100,y=140)
Button(root, text = 'RESET', font = 'arial 12 bold', command = Reset,             bg = 'Gray').place(x=170 , y =140)


#infinite loop to run program
root.mainloop()
