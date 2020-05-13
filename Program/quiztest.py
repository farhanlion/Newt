# -*- coding: cp1252 -*-
from Tkinter import *
import tkMessageBox
from PIL import Image, ImageTk
import methods
import mp3play
import pdb


def quiz(main_window, menuclip, typing_clip, music_playing):
    root = Toplevel()
    root.title("NEWTON'S LAWS OF MOTION - MINI QUIZ")
    methods.centralise(root, 625, 350)
    root.iconbitmap("images/newticon.ico")
    root.resizable(0, 0)
    musicname = 'sounds/calm.mp3'
    clip = mp3play.load(musicname)
    clip.play()

    global windows, windows3, windows4, windows5, windows6, windows7, count
    count = 0
    windows = Toplevel(root)
    windows.withdraw()
    windows.iconbitmap("images/newticon.ico")
    windows.title("Question 1")
    windows.geometry("610x400+400+200")
    windows.resizable(0, 0)

    windows3 = Toplevel(root)
    windows3.withdraw()
    windows3.iconbitmap("images/newticon.ico")
    windows3.title("Question 2")
    windows3.geometry("610x400+400+200")
    windows3.resizable(0, 0)

    windows4 = Toplevel(root)
    windows4.withdraw()
    windows4.iconbitmap("images/newticon.ico")
    windows4.title("Question 3")
    windows4.geometry("610x400+400+200")
    windows4.resizable(0, 0)

    windows5 = Toplevel(root)
    windows5.withdraw()
    windows5.iconbitmap("images/newticon.ico")
    windows5.title("Question 4")
    windows5.geometry("610x400+400+200")
    windows5.resizable(0, 0)

    windows6 = Toplevel(root)
    windows6.withdraw()
    windows6.iconbitmap("images/newticon.ico")
    windows6.title("Question 5")
    windows6.geometry("610x400+400+200")
    windows6.resizable(0, 0)

    windows7 = Toplevel(windows5)
    windows7.withdraw()
    windows7.iconbitmap("images/newticon.ico")
    windows7.title("Final Result")
    windows7.geometry("600x400+400+200")
    windows7.resizable(0, 0)

    # Background
    global total

    background = ImageTk.PhotoImage(Image.open('images/quizbg.jpeg'))
    panel = Label(root, image=background)
    panel.pack(fill="both", expand="yes")

    backgroundx1 = ImageTk.PhotoImage(Image.open('images/ques1.jpeg'))
    panel1 = Label(windows, image=backgroundx1)
    panel1.pack(fill="both", expand="yes")

    backgroundx2 = ImageTk.PhotoImage(Image.open('images/ques2.jpeg'))
    panel2 = Label(windows3, image=backgroundx2)
    panel2.pack(fill="both", expand="yes")

    backgroundx3 = ImageTk.PhotoImage(Image.open('images/ques3.jpeg'))
    panel3 = Label(windows4, image=backgroundx3)
    panel3.pack(fill="both", expand="yes")

    backgroundx4 = ImageTk.PhotoImage(Image.open('images/ques4.jpeg'))
    panel4 = Label(windows5, image=backgroundx4)
    panel4.pack(fill="both", expand="yes")

    backgroundx5 = ImageTk.PhotoImage(Image.open('images/ques5.jpeg'))
    panel5 = Label(windows6, image=backgroundx5)
    panel5.pack(fill="both", expand="yes")

    resultbackground = ImageTk.PhotoImage(Image.open('images/projectornew.jpeg'))

    # questions
    q = [

        "Acceleration of an object is dependent upon two variables \n- the net force acting \
upon the object and its mass.\nWhich law is this statement referring to?",
        "Referring to the formula 'F=ma',where F = force,\n m = mass and a = acceleration. \n\
What happens if the acceleration increases,\n provided that the mass is a constant?",
        "For every action, there is an ______ and ______ reaction. \nFill in the blanks.",
        "Which of the following is equivalent to the equation F=ma?",
        "A snooker of mass 150g ball was initially stationary.\n\
Referring to the formula F=ma, find the net force \n\
needed to move the ball at a speed of \n\
6 meter per second in a time of 0.05 seconds."
    ]

    a0 = ["Newton's First Law of Motion",
          "Newton's Second Law of Motion", "Newton's Third Law of Motion"]
    a1 = ["The force increases", "The force decreases",
          "There is no change in force."]
    a2 = ["equal, parallel", "unequal, opposite", "equal, opposite"]
    a3 = [" F = (mv-mu)/2t", " F = m(v-u)/t ", "F = (mv)/t(mu)"]
    a4 = ["18 N", "1.8 N", "-18 N"]

    def bnext():
        global cb1, cb2, cb3, windows, btn1, btn2, count
        root.withdraw()
        windows.deiconify()
        if count == 0:
            lbll = Label(windows, text=q[0], font=("Comic Sans MS bold", 11),
                         bg="black", fg='white')
            lbll.place(relx=0.55, rely=0.35, anchor=CENTER)
            count += 1

        cb1 = Radiobutton(windows, text=a0[0], value=0, variable=v0, activeforeground='blue',
                          cursor='hand2', font=("Comic Sans MS bold", 11))
        cb1.place(relx=0.5, rely=0.5, anchor=CENTER)
        cb2 = Radiobutton(windows, text=a0[1], value=1, variable=v0, activeforeground='blue',
                          cursor='hand2', font=("Comic Sans MS bold", 11))
        cb2.place(relx=0.515, rely=0.6, anchor=CENTER)
        cb3 = Radiobutton(windows, text=a0[2], value=2, variable=v0, activeforeground='blue',
                          cursor='hand2', font=("Comic Sans MS bold", 11))
        cb3.place(relx=0.505, rely=0.7, anchor=CENTER)
        btn1 = Button(windows, text="next", font=('arial', 12, 'bold'), cursor='gumby',
                      fg='black', bg='white', command=bnext2, relief=RAISED, bd=5)
        btn1.place(relx=0.85, rely=0.85, anchor=CENTER)
        btn2 = Button(windows, text="back", font=('arial', 12, 'bold'), cursor='gumby',
                      fg='black', bg='white', command=bback, relief=RAISED, bd=5)
        btn2.place(relx=0.15, rely=0.85, anchor=CENTER)
        windows.protocol("WM_DELETE_WINDOW", on_closing)

    def bnext2():
        global cb4, cb5, cb6, windows3, btn3, count
        windows.withdraw()
        windows3.deiconify()
        if count == 1:
            lbl2 = Label(windows3, text=q[1], font=("Comic Sans MS bold", 11),
                         bg="black", fg='white')
            lbl2.place(relx=0.55, rely=0.32, anchor=CENTER)
            count += 1

        cb4 = Radiobutton(windows3, text=a1[0], value=0, variable=v1, activeforeground='blue',
                          cursor='hand2', font=("Comic Sans MS bold", 11))
        cb4.place(relx=0.5, rely=0.5, anchor=CENTER)
        cb5 = Radiobutton(windows3, text=a1[1], value=1, variable=v1, activeforeground='blue',
                          cursor='hand2', font=("Comic Sans MS bold", 11))
        cb5.place(relx=0.505, rely=0.6, anchor=CENTER)
        cb6 = Radiobutton(windows3, text=a1[2], value=2, variable=v1, activeforeground='blue',
                          cursor='hand2', font=("Comic Sans MS bold", 11))
        cb6.place(relx=0.5525, rely=0.7, anchor=CENTER)
        btn3 = Button(windows3, text="next", font=('arial', 12, 'bold'), cursor='gumby',
                      fg='black', bg='white', command=bnext3, relief=RAISED, bd=5)
        btn3.place(relx=0.85, rely=0.85, anchor=CENTER)
        btn4 = Button(windows3, text="back", font=('arial', 12, 'bold'), cursor='gumby',
                      fg='black', bg='white', command=bback2, relief=RAISED, bd=5)
        btn4.place(relx=0.15, rely=0.85, anchor=CENTER)
        windows3.protocol("WM_DELETE_WINDOW", on_closing)

    def bnext3():
        global cb7, cb8, cb9, windows4, btn5, count
        windows3.withdraw()
        windows4.deiconify()
        if count == 2:
            lbl2 = Label(windows4, text=q[2], font=("Comic Sans MS bold", 11),
                         bg="black", fg='white')
            lbl2.place(relx=0.55, rely=0.33, anchor=CENTER)
            count += 1

        cb7 = Radiobutton(windows4, text=a2[0], value=0, variable=v2, activeforeground='blue',
                          cursor='hand2', font=("Comic Sans MS bold", 11))
        cb7.place(relx=0.49, rely=0.5, anchor=CENTER)
        cb8 = Radiobutton(windows4, text=a2[1], value=1, variable=v2, activeforeground='blue',
                          cursor='hand2', font=("Comic Sans MS bold", 11))
        cb8.place(relx=0.51, rely=0.6, anchor=CENTER)
        cb9 = Radiobutton(windows4, text=a2[2], value=2, variable=v2, activeforeground='blue',
                          cursor='hand2', font=("Comic Sans MS bold", 11))
        cb9.place(relx=0.495, rely=0.7, anchor=CENTER)
        btn5 = Button(windows4, text="next", font=('arial', 12, 'bold'), cursor='gumby',
                      fg='black', bg='white', command=bnext4, relief=RAISED, bd=5)
        btn5.place(relx=0.85, rely=0.85, anchor=CENTER)
        btn6 = Button(windows4, text="back", font=('arial', 12, 'bold'), cursor='gumby',
                      fg='black', bg='white', command=bback3, relief=RAISED, bd=5)
        btn6.place(relx=0.15, rely=0.85, anchor=CENTER)
        windows4.protocol("WM_DELETE_WINDOW", on_closing)

    def bnext4():
        global cb10, cb11, cb12, windows5, btn7, count
        windows4.withdraw()
        windows5.deiconify()
        if count == 3:
            lbl2 = Label(windows5, text=q[3], font=("Comic Sans MS bold", 11),
                         bg="black", fg='white')
            lbl2.place(relx=0.55, rely=0.32, anchor=CENTER)
            count += 1

        cb10 = Radiobutton(windows5, text=a3[0], value=0, variable=v3, activeforeground='blue',
                           cursor='hand2', font=("Comic Sans MS bold", 11))
        cb10.place(relx=0.48, rely=0.5, anchor=CENTER)
        cb11 = Radiobutton(windows5, text=a3[1], value=1, variable=v3, activeforeground='blue',
                           cursor='hand2', font=("Comic Sans MS bold", 11))
        cb11.place(relx=0.47, rely=0.6, anchor=CENTER)
        cb12 = Radiobutton(windows5, text=a3[2], value=2, variable=v3, activeforeground='blue',
                           cursor='hand2', font=("Comic Sans MS bold", 11))
        cb12.place(relx=0.47, rely=0.7, anchor=CENTER)
        btn7 = Button(windows5, text="next", font=('arial', 12, 'bold'), cursor='gumby',
                      fg='black', bg='white', command=bnext5, relief=RAISED, bd=5)
        btn7.place(relx=0.85, rely=0.85, anchor=CENTER)
        btn8 = Button(windows5, text="back", font=('arial', 12, 'bold'), cursor='gumby',
                      fg='black', bg='white', command=bback4, relief=RAISED, bd=5)
        btn8.place(relx=0.15, rely=0.85, anchor=CENTER)
        windows5.protocol("WM_DELETE_WINDOW", on_closing)

    def bnext5():
        global cb13, cb14, cb15, windows6, btn9, count
        windows5.withdraw()
        windows6.deiconify()
        if count == 4:
            lbl2 = Label(windows6, text=q[4], font=("Comic Sans MS bold", 11),
                         bg="black", fg='white')
            lbl2.place(relx=0.55, rely=0.3, anchor=CENTER)
            count += 1

        cb13 = Radiobutton(windows6, text=a4[0], value=0, variable=v4, activeforeground='blue',
                           cursor='hand2', font=("Comic Sans MS bold", 11))
        cb13.place(relx=0.495, rely=0.5, anchor=CENTER)
        cb14 = Radiobutton(windows6, text=a4[1], value=1, variable=v4, activeforeground='blue',
                           cursor='hand2', font=("Comic Sans MS bold", 11))
        cb14.place(relx=0.5, rely=0.6, anchor=CENTER)
        cb15 = Radiobutton(windows6, text=a4[2], value=2, variable=v4, activeforeground='blue',
                           cursor='hand2', font=("Comic Sans MS bold", 11))
        cb15.place(relx=0.5, rely=0.7, anchor=CENTER)
        btn9 = Button(windows6, text="Results", font=('arial', 12, 'bold'), cursor='gumby',
                      fg='black', bg='white', command=results, relief=RAISED, bd=5)
        btn9.place(relx=0.85, rely=0.85, anchor=CENTER)
        btn10 = Button(windows6, text="back", font=('arial', 12, 'bold'), cursor='gumby',
                       fg='black', bg='white', command=bback5, relief=RAISED, bd=5)
        btn10.place(relx=0.15, rely=0.85, anchor=CENTER)
        windows6.protocol("WM_DELETE_WINDOW", on_closing)

    # back button
    def bback():
        windows.withdraw()
        root.deiconify()

    def bback2():
        windows.deiconify()
        windows3.withdraw()

    def bback3():
        windows3.deiconify()
        windows4.withdraw()

    def bback4():
        windows4.deiconify()
        windows5.withdraw()

    def bback5():
        windows5.deiconify()
        windows6.withdraw()

    # next_button
    def next1():
        windows3.deiconify()
        windows.withdraw()

    def next2():
        windows4.deiconify()
        windows3.withdraw()

    def next3():
        windows5.deiconify()
        windows4.withdraw()

    def next4():
        windows6.deiconify()
        windows5.withdraw()

    def next5():
        windows7.deiconify()
        windows6.withdraw()

    class correction():

        def __init__(self, first, second, third, button, nexts):
            first['state'] = 'disabled'
            second['state'] = 'disabled'
            third['state'] = 'disabled'
            button.configure(command=nexts)

    # Tells the correct answer
    def checked():
        global total
        total = 0

        if v0.get() == 1:
            total += 1
            cb2.configure(bg='green')
        else:
            cb2.configure(bg='red')
        if v1.get() == 0:
            total += 1
            cb4.configure(bg='green')
        else:
            cb4.configure(bg='red')

        if v2.get() == 2:
            total += 1
            cb9.configure(bg='green')
        else:
            cb9.configure(bg='red')

        if v3.get() == 1:
            total += 1
            cb11.configure(bg='green')
        else:
            cb11.configure(bg='red')

        if v4.get() == 0:
            total += 1
            cb13.configure(bg='green')
        else:
            cb13.configure(bg='red')

    # Def backmm (back to main menu)
    def backmm():
        clip.stop()
        try:
            helproot
        except NameError:
            helproot_exists = False
        else:
            helproot_exists = True

        if helproot_exists:
            helproot.destroy()
        root.destroy()
        main_window.deiconify()
        methods.type(main_window, menuclip, typing_clip, music_playing)

    # Def Help Button
    def helpme():
        global helproot
        try:
            helproot
        except NameError:
            helproot = methods.helpwindow(root, 5)
        else:
            if helproot.winfo_exists() == 0:
                helproot = methods.helpwindow(root, 5)
            else:
                helproot.deiconify()

    # Marking Scheme
    def results():
        global windows7
        checked()
        windows6.withdraw()
        windows7.deiconify()
        if total == 5:
            panel1 = Label(windows7, image=resultbackground)
            panel1.pack()  # panel1.place(relx=0,rely=0)
            bf = Label(windows7, text="Score: " + str(total) + "/5",
                       font=("Comic Sans MS bold", 20), fg="blue", bg='white')
            bf.place(relx=0.5, rely=0.35, anchor=CENTER)
            bf1 = Label(windows7, text="Good Job!\n You have a strong understanding \n of Newton's Law of Motions.",
                        font=("Comic Sans MS bold", 11), fg='black',
                        bg='white', wraplength=300)
            bf1.place(relx=0.5, rely=0.55, anchor=CENTER)
        if total == 4 or total == 3:
            panel2 = Label(windows7, image=resultbackground)
            panel2.pack()  # panel2.place(relx=0,rely=0)
            bf = Label(windows7, text="Score: " + str(total) + "/5",
                       font=("Comic Sans MS bold", 20), fg="purple", bg='white')
            bf.place(relx=0.5, rely=0.35, anchor=CENTER)
            bf1 = Label(windows7, text="Nice Try!\n You have basic understanding \n of the topic but you need \n to work harder.",
                        font=("Comic Sans MS bold", 11), fg='black',
                        bg='white', wraplength=300)
            bf1.place(relx=0.5, rely=0.55, anchor=CENTER)
        if total < 3:
            panel3 = Label(windows7, image=resultbackground)
            panel3.pack()  # panel3.place(relx=0,rely=0)
            bf = Label(windows7, text="Score: " + str(total) + "/5",
                       font=("Comic Sans MS bold", 20), fg="red", bg='white')
            bf.place(relx=0.5, rely=0.35, anchor=CENTER)
            bf1 = Label(windows7, text="Fail!\n You have not understood \n Newton's Law of Motions. \n Go through the programmes again.",
                        font=("Comic Sans MS bold", 11), fg='black',
                        bg='white', wraplength=300)
            bf1.place(relx=0.5, rely=0.55, anchor=CENTER)
        btn100 = Button(windows7, cursor='gumby', text="Answers",
                        font=("Comic Sans MS", 12), fg='black',
                        bg='white', command=answers,
                        relief=RAISED, bd=5)
        btn100.place(relx=0.85, rely=0.94, anchor=CENTER)
        bquit = Button(windows7, text="Main Menu",
                       font=("Comic Sans MS", 12), fg='black',
                       bg='white', cursor='gumby', command=backmm,
                       relief=RAISED, bd=5)
        bquit.place(relx=0.15, rely=0.94, anchor=CENTER)
        windows7.protocol("WM_DELETE_WINDOW", on_closing)
        windows6.mainloop()

    # Showing Correct Answers
    def answers():
        btn2['state'] = 'disabled'
        windows7.withdraw()
        windows.deiconify()
        correction(cb1, cb2, cb3, btn1, next1)
        correction(cb4, cb5, cb6, btn3, next2)
        correction(cb7, cb8, cb9, btn5, next3)
        correction(cb10, cb11, cb12, btn7, next4)
        correction(cb13, cb14, cb15, btn9, next5)
        windows.mainloop()

    # Labels
    lbl0 = Label(root, text="MINI QUIZ", font=("Comic Sans MS", 22),
                 fg='white', bg='black', relief=SUNKEN, bd=5)
    lbl0.place(relx=0.5, rely=0.31, anchor=CENTER)
    lbl00 = Label(root, text="#all about Newton's Laws of Motion!",
                  font=("Comic Sans MS", 12), fg='white', bg='black',
                  relief=SUNKEN, bd=4)
    lbl00.place(relx=0.5, rely=0.44, anchor=CENTER)

    # Buttons
    beginbtn = Button(root, text="BEGIN", font=("Comic Sans MS", 12),
                      cursor='gumby', fg='white', bg='crimson',
                      relief=RAISED, bd=5, command=bnext)
    beginbtn.place(relx=0.5, rely=0.6, anchor=CENTER)

    mainmenubtn = Button(root, text="Main Menu", font=("Comic Sans MS", 12),
                         cursor='gumby', fg='white', bg='black',
                         relief=RAISED, bd=5, command=backmm)
    mainmenubtn.place(relx=0.87, rely=0.12, anchor=CENTER)

    helpbut = Button(root, text="Help", font=("Comic Sans MS", 12),
                     cursor='gumby', fg='white', bg='black',
                     relief=RAISED, bd=5, command=helpme)
    helpbut.place(relx=0.72, rely=0.12, anchor=CENTER)

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
    music_on = Button(root, text="ON", command=musicon,
                      font=("Comic Sans MS", 10), fg='white',
                      bg='black', relief=RAISED, bd=3,
                      state="disabled", width=6)
    music_on.place(relx=0.065, rely=0.21, anchor=CENTER)

    music_off = Button(root, text="OFF", command=musicoff,
                       font=("Comic Sans MS", 10), fg='white',
                       bg='black', relief=RAISED, bd=3, width=7)
    music_off.place(relx=0.17, rely=0.21, anchor=CENTER)

    music_label = Label(root, text="Music Status:", font=("Comic Sans MS", 12),
                        relief=SUNKEN, bd=3, fg='white', bg="black", width=12)
    music_label.place(relx=0.12, rely=0.11, anchor=CENTER)

    # Ask User whether wants to exit or not
    def on_closing():
        if tkMessageBox.askokcancel("Quit", "Do you want to go back to Main Menu?"):
            backmm()

    v0 = IntVar()
    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
