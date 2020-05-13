from Tkinter import *
import pdb
import random
import mp3play


def helpwindow(gameroot, gameroot_num):
    global clip
    helproot = Toplevel()
    helproot.resizable(0, 0)
    helproot.title("Help")
    helproot.iconbitmap("images/newticon.ico")
    helproot.configure(bg='royalblue4')

    instructions = ""
    ins_width = 0
    ins_height = 0
    if gameroot_num == 1:
        centralise(helproot, 450, 500)
        instructions = '1. Click \'Begin Animation\' button on the bottom left to start the animation. \n\n\
2. Click the \'Reset\' button on the bottom right to reset the animation. \n\n\
3. Click the \'Main Menu\' button on the top right corner to exit to main menu. \n\n\
4. Select\'ON\' or \'OFF\' on the top left to turn the background music on or off!'
        ins_height = 12
        ins_width = 40
        ins_wraplength = 400
    elif gameroot_num == 2:
        centralise(helproot, 400, 450)
        instructions = '1. Adjust the scale to specify the magnitude of force to apply on the ball.\n\n\
2. Click \'Start\' to push the ball. \n\n\
There are some objectives too!\n\
Enjoy :)'
        ins_height = 10
        ins_width = 30
        ins_wraplength = 300
    elif gameroot_num == 3:
        centralise(helproot, 600, 600)
        instructions = '1. Click the \'Rocket\' button on the bottom left to choose one of the three rockets.\n\n\
2. Move the Scale on the right to apply thrust.\n\n\n\
Theory:\n\n\
When the thrust of the rocket pushes the fuel downwards, the fuel will produce an equal and opposite force pushing the rocket upwards. \
Once the thrust overcomes the weight of the rocket, the rocket will fly up into space.\
The force Diagram situated at the bottom right corner illustrates this behaviour of the balance of forces on the rocket.'
        ins_height = 15
        ins_width = 54
        ins_wraplength = 540
    elif gameroot_num == 4:
        centralise(helproot, 450, 475)
        instructions = '1. Choose a Newton\'s Law for an engaging tutorial session.\n\n\
2. Click the \'Mini Quiz\' to assess yourself.\n\n\
3. Refer to the User Guide if you get stuck.\n\n\n\
P.S. Don\'t forget to have fun!'
        ins_height = 11
        ins_width = 40
        ins_wraplength = 400

    elif gameroot_num == 5:
        centralise(helproot, 700, 675)
        instructions = "Mini Quiz: This section requires you to apply what you have learnt. Guidaince & Descriptions:\n\n\
1. There will be 5 questions, each with 3 choices of answer.\n\n\
2. Select your answer according to your knowledge from the previous 3 interactive sections.\n\n\
3. Proceed by clicking 'next'. If you wish to change your answer, click 'back' to see the previous questions and amend your answer.\n\n\
4. Your results will be shown on the final page.\n\n\
5. To view the correct answers, click 'Answers' on the final result page.\n\n\
6. Click 'Main Menu' to return back to Main Menu."
        ins_height = 18
        ins_width = 60
        ins_wraplength = 600
    elif gameroot_num == 6:
        centralise(helproot, 600, 260)
        instructions = 'Weight = Mass x gravitational acceleration\n\n *Note: the value of gravitational acceleration, g is  9.81ms^(-2)'
        ins_height = 5
        ins_width = 52
        ins_wraplength = 520

    elif gameroot_num == 7:
        centralise(helproot, 550, 275)
        instructions = 'The acceleration of rocket is found using Newtons\'s Second Law:\n\n\
Force = Mass x Acceleration'
        ins_height = 6
        ins_width = 45
        ins_wraplength = 450

    def back():
        helproot.destroy()

    titletext = Label(helproot, text="Help",
                      font=("Comic Sans MS bold", 20), relief='flat', bd=5,
                      bg='royalblue4', fg='white', width=10, height=1)
    titletext.place(relx=0.5, rely=0.1, anchor=CENTER)

    helplabel = Label(helproot, text=instructions, font=("Comic Sans MS", 13), wraplength=ins_wraplength,
                      fg="white", bg="steel blue", relief='ridge', bd=1, height=ins_height, width=ins_width, justify=LEFT)

    helplabel.place(relx=0.5, rely=0.20, anchor='n')

    if gameroot_num == 1:
        back_btn = Button(helproot, text="Back", relief=RAISED,
                          font=("Comic Sans MS", 14), fg='white',
                          bg="steel blue", bd=2, command=back, height=1, width=10)
        back_btn.place(relx=0.5, rely=0.90, anchor=CENTER)
        helplabel.place(relx=0.5, rely=0.20, anchor='n')
    elif gameroot_num == 2:
        back_btn = Button(helproot, text="Back", relief=RAISED,
                          font=("Comic Sans MS", 14), fg='white',
                          bg="steel blue", bd=2, command=back, height=1, width=10)
        back_btn.place(relx=0.5, rely=0.878, anchor=CENTER)
        helplabel.place(relx=0.5, rely=0.20, anchor='n')
    elif gameroot_num == 3:
        back_btn = Button(helproot, text="Back", relief=RAISED,
                          font=("Comic Sans MS", 14), fg='white',
                          bg="steel blue", bd=2, command=back, height=1, width=10)
        back_btn.place(relx=0.5, rely=0.90, anchor=CENTER)
        helplabel.place(relx=0.5, rely=0.20, anchor='n')
    elif gameroot_num == 4:
        back_btn = Button(helproot, text="Back", relief=RAISED,
                          font=("Comic Sans MS", 14), fg='white',
                          bg="steel blue", bd=2, command=back, height=1, width=10)
        back_btn.place(relx=0.5, rely=0.90, anchor=CENTER)
        helplabel.place(relx=0.5, rely=0.20, anchor='n')
    elif gameroot_num == 5:
        back_btn = Button(helproot, text="Back", relief=RAISED,
                          font=("Comic Sans MS", 14), fg='white',
                          bg="steel blue", bd=2, command=back, height=1, width=10)
        back_btn.place(relx=0.5, rely=0.90, anchor=CENTER)
        titletext.place(relx=0.5, rely=0.08, anchor=CENTER)
        helplabel.place(relx=0.5, rely=0.16, anchor='n')
    elif gameroot_num == 6:
        back_btn = Button(helproot, text="Back", relief=RAISED,
                          font=("Comic Sans MS", 14), fg='white',
                          bg="steel blue", bd=2, command=back, height=1, width=10)
        back_btn.place(relx=0.5, rely=0.84, anchor=CENTER)
        titletext.destroy()
        helplabel.configure(justify=CENTER)
        helplabel.place(relx=0.5, rely=0.20, anchor='n')
    elif gameroot_num == 7:
        back_btn = Button(helproot, text="Back", relief=RAISED,
                          font=("Comic Sans MS", 14), fg='white',
                          bg="steel blue", bd=2, command=back, height=1, width=10)
        back_btn.place(relx=0.5, rely=0.85, anchor=CENTER)
        titletext.destroy()
        helplabel.place(relx=0.5, rely=0.15, anchor='n')

    return helproot


# Only for Main Menu
def type(main_window, clip, typing_clip, music_playing):
    global afterid, typing
    if music_playing:
        clip.play()

    def wait(delay):
        global afterid
        var = IntVar()
        afterid = main_window.after(delay, var.set, 1)
        main_window.wait_variable(var)

    message = Label(main_window, fg='white', font=("Comic Sans MS", 12),
                    relief='ridge', bd=5, bg='royalblue4',
                    text="", anchor=W, wraplength=800,
                    justify=LEFT, width=80, height=2)
    message.place(relx=0.1, rely=0.87)

    def typewriter(text, delay):
        global afterid
        typing_clip.play()

        def wait():
            global afterid
            var = IntVar()
            afterid = main_window.after(delay, var.set, 1)
            main_window.wait_variable(var)
        message_text = text
        message_display = ""
        for letter in message_text:
            message_display += letter
            wait()
            message.configure(text=message_display)
        typing_clip.stop()

    global dyk
    dyk = [
        "Isaac Newton was born on 4 January 1643, the same year Galileo died, in Woolsthorpe, England. ",
        "Isaac Newton is a scientist, mathematician, physicist, theologian, author and an astronomer. ",
        "Isaac Newton was enrolled at the King's School in Grantham, a town in Lincolnshire. ",
        "Isaac Newton's mom pulled him out of school at age 12 and planned to make him a farmer. ",
        "The unit for Force is Newtons (N), named after the scientist called Isaac Newton. ",
        "If the noble prizes had been around during Isaac Newton's lifetime, he would have won it hands down in multiple years. ",
        "Isaac Newton became a mathematics professor at Cambridge University at the age of 27.",
        "Isaac Newton was very secretive during his entire career.",
        "Isaac Newton suffered twice a nervous breakdown and he suspected that his friends conspired against him.",
        "[What we know is a drop, what we don't know is an ocean.] - Isaac Newton"
    ]
    typing = True
    while typing:
        instructions = dyk[random.randint(0, 9)]
        typewriter(instructions, 30)
        wait(6000)


def stoptyping(main_window):
    global typing
    typing = False
    main_window.after_cancel(afterid)


def centralise(window, window_width, window_height):
    screen_height = window.winfo_screenheight()
    screen_width = window.winfo_screenwidth()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2.18) - (window_height / 2)
    window.geometry('%dx%d+%d+%d' %
                    (window_width, window_height, x_coordinate, y_coordinate))
