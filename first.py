from pytube import YouTube
import tkinter 
from tkinter.filedialog import *
def download():
    print('dhffhgvjhbkhjnkjnkjn',E1)

    #videos=yt.streams.filter(progressive=True, file_extension='mp4')
    path=askdirectory()
    yt=YouTube(E1.get()).streams.first().download(path)
    print(yt)
    '''print(path)
    i=1
    for stream in videos:
        print(str(i) +"---"+ str(stream))
        print(stream.resolution)

        i+=1
    stm_no=int(input('enter no.'))
    video=videos[stm_no-1]
    video.download(path)'''
    print('Downloaded')
    l=Label(win, text='Downloaded')
    l.pack()

if __name__== '__main__':
    win=Tk()
    E1=Entry(win)
    E1.pack()
    #win.mainloop()
    #link = input('Enter youtube link')
    #link=E1
    #yt=YouTube(link)
    b = Button(win,text='okay',command = download)
    b.pack(side='bottom')
    win.mainloop()

