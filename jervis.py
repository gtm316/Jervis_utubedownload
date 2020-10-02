import pyttsx3
import tkinter
from tkinter import *
from tkinter import filedialog
import datetime
import wikipedia
import smtplib
import random
import os
import speech_recognition as sr
print(os.getcwd())
eng=pyttsx3.init('sapi5')
voice=eng.getProperty('voices')
print(voice[0].id)
eng.setProperty('voice', voice[0].id)
def speak(audio):
    eng.say(audio)
    eng.runAndWait()
def wishme():
    hr=int(datetime.datetime.now().hour)
    if hr<12:
        speak('Good Morning')
    elif hr>=12 and hr<18:
        speak('Good afternoon')
    else:
        speak('Good evening')
    speak ('I am Guddu, How may i help u sir')

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    uname='316gsharm@gmail.com'
    pwd='3169967346524'
    server.login(uname,pwd)
    server.sendmail(uname,to,content)
    server.close()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak('listening......')
        r.pause_threshold = 1   #Gap while speaking
        r.energy_threshold = 500    # for removing bg voice
        audio=r.listen(source)

    try:

        print('Recognizing....')
        q=r.recognize_google(audio, language='en-in')
        print(f'user said {q}\n')
    except Exception as e:
        print(e)
        speak('say that again')
        return 'None'
    return q



if __name__=='__main__':

    print('wishing ')
    wishme()

    while 1:
        query=takecommand().lower()
        print(query)
        if 'wikipedia' in query:
            speak('searching wiki...')
#            l3=tk.Label(root, text='Searching for wikipedia...')
#            l3.pack()
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query, sentences=2, auto_suggest=True)
#            result=wikipedia.summary(query, sentence=2
            speak('As per wikipedia')
#            l2=tk.Label(root, text=result, font='Times 32')
#            l2.pack()
            speak(result)
            print(result)

        elif 'email' in query:
            try:
                speak('What should i do')
                content=takecommand()
                to='gautamsharma564@yahoo.com'
                sendEmail(to,content)
                speak('Email sent')
            except Exception as e:
                print(e)
                speak('We are unable to send email')
        elif 'play music' or 'play movies' in query:
            root=Tk()
            root.title('Media')
            root.geometry('200x100')
            def folder():
              
                filename=filedialog.askdirectory()
                musc_dir=filename
                song=random.choice(os.listdir(musc_dir))
                print(song)
                os.startfile(os.path.join(musc_dir,song))
                print(filename)
                root.destroy
                return True
            #    fp.set(filename)

            btn=Button(text='Browse file', command=folder)
            btn.pack()
            
            mainloop()


#            musc_dir='F:\Links\MyDesktop\pacl'
           

#root=tk.mainloop()








