from Tkinter import *
from PIL import Image, ImageTk
import tkMessageBox
import time
import mp3play
import random
import Newtonlaw1
import Newtonlaw2
import Newtonlaw3
import quiztest
import creditsgiveto
import methods
import sys

typing_clip = mp3play.load('sounds/typing.mp3')
musicname = 'sounds/sunshinemenu.mp3'
clip = mp3play.load(musicname)
intromusicname = 'sounds/sunshineintro.mp3'
introclip = mp3play.load(intromusicname)
musicname = 'sounds/successsong.mp3'
creditsclip = mp3play.load(musicname)


def first_law():
    info = False
    clip.stop()
    typing_clip.stop()
    helproot_exists = checkhelproot()
    creditroot_exists = checkcreditroot()
    if helproot_exists:
        helproot.destroy()
    if creditroot_exists:
        creditroot.destroy()
    main_window.withdraw()
    methods.stoptyping(main_window)
    music_playing = checkmusic()
    Newtonlaw1.Newtons_First_Law(main_window, clip, typing_clip, music_playing)


def second_law():
    info = False
    clip.stop()
    typing_clip.stop()
    helproot_exists = checkhelproot()
    creditroot_exists = checkcreditroot()
    if helproot_exists:
        helproot.destroy()
    if creditroot_exists:
        creditroot.destroy()
    main_window.withdraw()
    methods.stoptyping(main_window)
    music_playing = checkmusic()
    Newtonlaw2.Newtons_Second_Law(
        main_window, clip, typing_clip, music_playing)


def third_law():
    info = False
    clip.stop()
    typing_clip.stop()
    helproot_exists = checkhelproot()
    creditroot_exists = checkcreditroot()
    if helproot_exists:
        helproot.destroy()
    if creditroot_exists:
        creditroot.destroy()
    main_window.withdraw()
    methods.stoptyping(main_window)
    music_playing = checkmusic()
    Newtonlaw3.Newtons_Third_Law(main_window, clip, typing_clip, music_playing)


def quizz():
    clip.stop()
    typing_clip.stop()
    helproot_exists = checkhelproot()
    creditroot_exists = checkcreditroot()
    if helproot_exists:
        helproot.destroy()
    if creditroot_exists:
        creditroot.destroy()
    main_window.withdraw()
    methods.stoptyping(main_window)
    music_playing = checkmusic()
    quiztest.quiz(main_window, clip, typing_clip, music_playing)


def creditsto():
    global creditroot
    clip.stop()
    typing_clip.stop()
    helproot_exists = checkhelproot()
    creditroot_exists = checkcreditroot()
    if helproot_exists:
        helproot.destroy()
    if creditroot_exists:
        creditroot.destroy()
    methods.stoptyping(main_window)
    music_playing = checkmusic()
    creditroot = creditsgiveto.creditfor(
        main_window, clip, typing_clip, music_playing)


def checkhelproot():
    try:
        helproot
    except NameError:
        return False
    else:
        return True


def checkcreditroot():
    try:
        creditroot
    except NameError:
        return False
    else:
        return True


def checkmusic():
    if str(music_on['state']) == 'disabled':
        return True
    else:
        return False


def intro():
    def text(content, time, fontsize):
        global master
        master = Tk()
        label = Label(text=(str(content)), font=(
            "Comic Sans MS", fontsize), fg='black', bg='white', highlightthickness=0)
        label.master.overrideredirect(True)
        window_width = label.winfo_reqwidth()
        window_height = label.winfo_reqheight()

        screen_height = label.master.winfo_screenheight()
        screen_width = label.master.winfo_screenwidth()
        x_coordinate = (screen_width/2)-(window_width/2)
        y_coordinate = (screen_height/2.75)-(window_height/2)
        label.master.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

        label.master.lift()
        label.master.wm_attributes("-topmost", True)
        if sys.platform == 'win32':
            label.master.wm_attributes("-disabled", True)
            label.master.wm_attributes("-transparentcolor", "white")
        else:
            label.master.wm_attributes("-alpha", True)
        label.master.wait_visibility(master)
        label.after(time, label.master.destroy)
        label.pack()

    introclip.play()
    text("Welcome to Newt!", 3333, 80)
    master.mainloop()
    text("You will be going through all the 3 laws of motions \n\
    discovered by Isaac Newton today!", 3333, 25)
    master.mainloop()
    text("Choose any laws to start with by clicking the buttons. \n\
    Enjoy!", 3333, 25)
    master.mainloop()
    introclip.stop()


def close_window():
    creditsclip.stop()
    clip.stop()
    typing_clip.stop()
    methods.stoptyping(main_window) 
    main_window.destroy()

def helpme():
    global helproot
    try:
        helproot
    except NameError:
        helproot = methods.helpwindow(master, 4)
    else:
        if helproot.winfo_exists() == 0:
            helproot = methods.helpwindow(master, 4)
        else:
            helproot.deiconify()

    creditroot_exists = checkcreditroot()
    if creditroot_exists:
        creditroot.destroy()
        music_playing = checkmusic()
        methods.type(main_window, clip, typing_clip, music_playing)


def window():
    global main_window, music_on
   
    main_window = Tk()
    methods.centralise(main_window,1000,580)
    main_window.title("Newton's Laws of Motion")
    main_window.iconbitmap("images/newticon.ico")
    main_window.wm_attributes("-topmost", False)
    
    
    main_window.resizable(0, 0)
    background = ImageTk.PhotoImage(Image.open('images/bluepixels.png'))
    panel = Label(main_window, image=background)
    panel.pack(side='top', fill="both", expand="yes")
    panel.image = background
    
    main_window.protocol("WM_DELETE_WINDOW", close_window)

    newtlabelx = Label(main_window, text="WELCOME TO NEWT",
                       font=("Comic Sans MS", 37), fg='white', bg='royalblue4',
                       relief=SUNKEN, bd=5, width=18, height=1)
    newtlabelx.place(relx=0.1, rely=0.2)

    newton1_button = Button(main_window, text="Newton's First Law", bd=3,
                            bg='royalblue1', width=30, height=1,
                            font=("Comic Sans MS", 12), fg='white',
                            command=first_law)
    newton1_button.place(relx=0.1, rely=0.45)

    newton2_button = Button(main_window, text="Newton's Second Law", bd=3,
                            bg='royalblue2', width=30, height=1,
                            font=("Comic Sans MS", 12), fg='white',
                            command=second_law)
    newton2_button.place(relx=0.1, rely=0.522)

    newton3_button = Button(main_window, text="Newton's Third Law", bd=3,
                            bg='royalblue3', width=30, height=1,
                            font=("Comic Sans MS", 12), fg='white',
                            command=third_law)
    newton3_button.place(relx=0.1, rely=0.594)

    quiz_button = Button(main_window, text="Mini Quiz", bd=3,
                         bg='royalblue4', width=30, height=1,
                            font=("Comic Sans MS", 12), fg='white',
                         command=quizz)
    quiz_button.place(relx=0.1, rely=0.667)

    exit_button = Button(main_window, text="Exit", bd=4, bg='lightblue2',
                         width=6, height=1, font=("Comic Sans MS", 12),
                         fg='royalblue4', command=close_window)
    exit_button.place(relx=0.9, rely=0.05)

    help_button = Button(main_window, text="Help", bd=4, bg='lightblue2',
                         width=4, height=1, font=("Comic Sans MS", 12),
                         fg='royalblue4', command=helpme)
    help_button.place(relx=0.84, rely=0.05)

    credits_button = Button(main_window, text="Credits", bd=4,
                            bg='lightblue2', width=6, height=1,
                            font=("Comic Sans MS", 12), fg='royalblue4',
                            command=creditsto)
    credits_button.place(relx=0.76, rely=0.05)
    
    # Def Music On:

    def musicon():
        clip.play()
        music_on.config(state=DISABLED, fg="grey")
        music_off.config(state=NORMAL, fg="white")

    # Def Music Off:

    def musicoff():
        clip.stop()
        music_on.config(state=NORMAL, fg="white")
        music_off.config(state=DISABLED, fg="grey")

    # Music
    music_label = Label(main_window, text="Music Status:",
                        font=("Comic Sans MS", 14), fg='royalblue4',
                        bg='lightblue2', height=1)
    music_label.place(relx=0.082, rely=0.051, anchor=CENTER)

    music_on = Button(main_window, text="ON", relief=RAISED, fg='white',
                      command=musicon, font=("Comic Sans MS bold", 10),
                      width=6,  bg='royalblue4', bd=3, state=DISABLED)
    music_on.place(relx=0.051, rely=0.1183, anchor=CENTER)

    music_off = Button(main_window, text="OFF", relief=RAISED, fg='white',
                       command=musicoff, font=("Comic Sans MS bold", 10),
                       width=6, bg='royalblue4', bd=3, state=NORMAL)
    music_off.place(relx=0.112, rely=0.1183, anchor=CENTER)
    music_playing = True
    # Typewriter
    newtlabeltw = Label(main_window, text="Do You Know?", relief='ridge', bd=5,
                        font=("Comic Sans MS", 16), fg='white',
                        bg='royalblue4')
    newtlabeltw.place(relx=0.1, rely=0.8)

    methods.type(main_window, clip, typing_clip, music_playing)

intro()
window()
