# -*- coding: cp1252 -*-
from Tkinter import *
from PIL import Image, ImageTk
import os
import mp3play
import tkMessageBox
import methods


def creditfor(main_window, menuclip, typing_clip, music_playing):
    global clip, musicname
    root = Toplevel()
    root.grab_set()
    methods.centralise(root, 350, 350)
    root.resizable(0, 0)
    root.title("Credits")
    root.iconbitmap("images/newticon.ico")
    musicname = 'sounds/successsong.mp3'
    creditsclip = mp3play.load(musicname)
    creditsclip.play()
    background = ImageTk.PhotoImage(Image.open('images/darkgold.jpeg'))
    panel = Label(root, image=background)
    panel.pack(side='top', fill="both", expand="yes")
    panel.image = background

    def on_closing():
        creditsclip.stop()
        root.destroy()
        methods.type(main_window, menuclip, typing_clip, music_playing)

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Def Main Menu Button

    def back():
        creditsclip.stop()
        root.destroy()
        methods.type(main_window, menuclip, typing_clip, music_playing)

    titletext = Label(root, text="Credits To",
                      font='castellar 18 bold', relief=RIDGE, bd=5,
                      bg='gold', fg='black')
    titletext.place(relx=0.5, rely=0.07, anchor=CENTER)

    creditlabel = Label(root, text="CA Team 3 \n\
----------------------\n\
(1) Mohamad Farhan Ahsan\n\
(2) Toh Zheng Aun \n\
(3) Andrew Ling Xian Hann \n\
(4) Theodore Lau Hui You \n\
\n\
@allrightsreserved \n\
@copyright2020", font=("Comic Sans MS bold", 11),
        fg="white", bg="black", bd=5, height=11, width=25, justify=LEFT)
    creditlabel.place(relx=0.5, rely=0.5, anchor=CENTER)

    back_btn = Button(root, text="Back", relief=RAISED,
                      font=("Comic Sans MS", 12), fg='white',
                      bg="black", bd=5, command=back, height=1)
    back_btn.place(relx=0.5, rely=0.92, anchor=CENTER)
    return root
