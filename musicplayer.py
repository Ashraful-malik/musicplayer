import tkinter.messagebox as msg
from tkinter import ttk
from pygame import mixer
from tkinter import filedialog
import datetime
from mutagen.mp3 import MP3
from tkinter import *
def add():
        global path
        path=filedialog.askopenfilename(defaultextension=".mp3",filetypes=[("MP3 Files","*.mp3")])
        listbox.insert(0,path)
def play():
    try:
        select = listbox.curselection()
        musicplay = listbox.get(select)
        mixer.music.load(musicplay)
        mixer.music.play(loops=1)
        # it give us length of songs
        song=MP3(path)
        songlength=int(song.info.length)
        progressbar['maximum'] =songlength
        songend.config(text='{}'.format(str(datetime.timedelta(seconds=songlength))))
        def musics():
            # it give us crunt music play time
            progressbarlength=mixer.music.get_pos()//1000
            button1.config(text='{}'.format(str(datetime.timedelta(seconds=progressbarlength))))

            progressbar['value']=progressbarlength
            progressbar.after(1,musics)

        musics()
    except Exception:
        msg.showerror("warning","song is not selected")


def pause():
    mixer.music.pause()
    pause.grid_remove()
    resume.grid()
def resume():
    mixer.music.unpause()
    resume.grid_remove()
    pause.grid()
def stop():
    mixer.music.stop()
def volume(vol):
    a=int(vol)
    volume=a/100
    mixer.music.set_volume(volume)
window=Tk()
window.geometry("550x400")
window.title("Music player")
window.resizable(False,False)


play2img=PhotoImage(file='play2.png')
playimg=PhotoImage(file='play.png')
stopimg=PhotoImage(file='stop.png')
pauseimg=PhotoImage(file='pause.png')
icon=PhotoImage(file='video.png')
window.iconphoto(True,icon)

title_text=Label(window,text="Music player",font="Algerian 25 underline",
    foreground="#358DD4")
sound=Label(window,text="sound",font="arial 20 ",fg="#5872F5")
listbox=Listbox(window,width=40,height=10,selectmode=EXTENDED)
progressbar=ttk.Progressbar(window,mode='determinate',length=350)


# buttons
button1=Button(window,text="0.00",width=10,relief="groove")
songend=Button(window,text="0.00",width=10,relief="groove")
openfile=Button(window,text="ADD+",width=10,command=add,relief="groove",fg="red",borde=2)
play=Button(window,text="open",image=play2img,command=play)
pause=Button(window,text="pause",image=pauseimg,command=pause)
resume=Button(window,text="resume",image=playimg,command=resume)
stop=Button(window,text="stop",image=stopimg,command=stop)

slider=Scale(window,orient='vertical',length=180,from_=100,to=1,command=volume,fg="blue",
troughcolor="#1E90FF",  relief="sunken", borderwidth=0,sliderrelief="groove",    font="arial 10 bold" )


# pack
title_text.grid(row=0,column=1)
listbox.grid(row=1,column=1)
openfile.grid(row=2,column=1)
play.grid(row=3,column=0,padx=10)
pause.grid(row=3,column=1,pady=5)
resume.grid(row=3,column=1,pady=5)
stop.grid(row=3,column=2)
slider.grid(row=1,column=2)
sound.grid(row=2,column=2)
progressbar.grid(row=4,column=1)
button1.grid(row=4,column=0)
songend.grid(row=4,column=2)
resume.grid_remove()
mixer.init()
window.mainloop()