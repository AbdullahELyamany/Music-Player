
"""
 Music Player
 
 Created by *Abdullah EL-Yamany*
"""

import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os



def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
    
def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    #print(Music_Name(ACTIVE))
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()






# ========================== GUI Tkinter =========================== #

root = Tk()
#root.geometry("485x700+290+10")
#root.title("Music Player")
root.configure(background = "#333333")
#root.resizeable(False, False)

mixer.init()


frameCnt = 30
frames = [PhotoImage(file = "music.gif", format = 'gif -index %i'%(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0

    label.configure(image=frame)
    root.after(40, update, ind)

label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)



lower_frame = Frame(root, bg="#FFFFFF", width=802, height=200)
lower_frame.place(x=0, y=600)


#image_icon = PhotoImage(file="")
#root.iconphoto(False, image_icon)

Menu = PhotoImage(file="")
Label(root, image=Menu).place(x=0, y=800, width=803, height = 360)


Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=800, width=802, height=360)


ButtonPlay = PhotoImage(file = "play.png")
Button(
    root,
    image = ButtonPlay,
    bg="#FFFFFF",
    bd = 0,
    height = 100,
    width = 100,
    command = PlayMusic,
).place(x = 310, y=610)

ButtonStop = PhotoImage(file = "stop.png")
Button(
    root,
    image = ButtonStop,
    bg="#FFFFFF",
    bd = 0,
    height = 100,
    width = 100,
    command = mixer.music.stop,
).place(x = 190, y=610)

Buttonpause = PhotoImage(file = "pause.png")
Button(
    root,
    image = Buttonpause,
    bg="#FFFFFF",
    bd = 0,
    height = 100,
    width = 100,
    command = mixer.music.pause,
).place(x = 430, y=610)

Buttonresume = PhotoImage(file = "resume.png")
Button(
    root,
    image = Buttonresume,
    bg="#FFFFFF",
    bd = 0,
    height = 100,
    width = 100,
    command = mixer.music.unpause,
).place(x = 550, y=610)


Volume1 = PhotoImage(file = "volume.png")
pane1 = Label(root, image = Volume1, width=100, height=100, bg="#FFFFFF",).place(x=20, y = 610)


Button(
    root,
    text="Browse Music",
    width=33,
    height=1,
    font=("calibri", 12, "bold"),
    fg = "Black",
    bg = "#FFFFFF",
    command = AddMusic
).place(x=9, y = 728)


Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(
               Frame_Music,
               width=100,
               font = ("Times new roman", 10),
               bg="#333333",
               fg="gray",
               selectbackground = "lightblue",
               cursor = "hand2",
               bd=0,
               yscrollcommand = Scroll.set,
           )
Scroll.configure(command = Playlist.yview)
Scroll.pack(side = RIGHT, fill = Y)
Playlist.pack(side = RIGHT, fill = BOTH)



root.mainloop()
