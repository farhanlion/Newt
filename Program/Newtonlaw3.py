from Tkinter import *
import tkMessageBox
from PIL import Image, ImageTk
import time
import pdb
import mp3play
import methods


def Newtons_Third_Law(main_window, menuclip, typing_clip, music_playing):
    root3 = Toplevel()
    methods.centralise(root3, 700, 700)
    root3.resizable(0, 0)
    root3.title("NEWTON'S THIRD LAW OF MOTION")
    root3.iconbitmap("images/newticon.ico")
    frame_title = Frame(root3)
    frame_title.pack(side=TOP, fill="both", expand=True)
    frame_title.configure(bg='royalblue4')
    frame_scale = Frame(root3)
    frame_scale.place(x=420, y=150)
    clip2 = mp3play.load('sounds/launch.mp3')

    global weight, mass, u, v, s, t, position, land2, sky, change
    mass = 0
    change = 0
    weight = 0
    thrust = 0
    acceleration1 = 0
    position = [0, 0, 0, 0]
    t = 0
    u = 0
    v = 1
    s = 1

    # Canvas
    animation = Canvas(root3, width=300, height=400,
                       relief='ridge', bd=3, bg='black')
    animation.place(x=20, y=100)

    force_diagram = Canvas(root3, width=150, height=150,
                           relief='ridge', bd=3, bg='lightblue')
    force_diagram.place(x=430, y=470)
    # Images

    # Typewriter label
    message = Label(root3, fg='white', font=("Comic Sans MS", 12), relief='ridge', bd=5,
                    bg='steel blue', text="", anchor=W, wraplength=630, justify=LEFT, width=68, height=2)
    message.place(relx=0.005, rely=0.905)

    # typewriter function

    def waitforcontinue():
        global new_button

        var = BooleanVar()
        new_button = Button(root3, bd=5,
                            bg='royalblue4', fg='white', font=("Comic Sans MS", 12), text="Next",
                            command=lambda: var.set(True))
        new_button.place(relx=0.9, rely=0.913)
        new_button.wait_variable(var)
        new_button.destroy()

    def typewriter(text, delay):
        typing_clip.play()

        def wait():
            var = IntVar()
            root3.after(delay, var.set, 1)
            root3.wait_variable(var)
        message_text = text
        message_display = ""

        for letter in message_text:
            message_display += letter
            wait()
            message.configure(text=message_display)
        typing_clip.stop()
    # Land
    land1 = ImageTk.PhotoImage(Image.open("images/land.jpeg"))
    land2 = animation.create_image(0, 430, anchor=SW, image=land1)

    # sky
    sky1_2 = ImageTk.PhotoImage(Image.open("images/sky.png"))
    sky = animation.create_image(0, -1400, anchor=NW, image=sky1_2)

    # rocket
    rocket1_2 = ImageTk.PhotoImage(Image.open("images/new_rocket1.png"))

    rocket2_2 = ImageTk.PhotoImage(Image.open("images/new_rocket2.png"))

    rocket3_2 = ImageTk.PhotoImage(Image.open("images/new_rocket3.png"))

    # fire
    fire2 = ImageTk.PhotoImage(Image.open("images/new_fire.png"))

    # people
    people = ImageTk.PhotoImage(Image.open("images/people.png"))
    people2 = animation.create_image(-420, 125, anchor=NW, image=people)

    # launchpad
    launchpad1 = ImageTk.PhotoImage(Image.open("images/launchpad.png"))
    launchpad2 = animation.create_image(-230, -15, anchor=NW, image=launchpad1)

    # force diagram
    points = [(75, 135), (55, 105), (65, 105),
              (65, 75), (85, 75), (85, 105), (95, 105)]
    points2 = [(75, 15), (55, 45), (65, 45), (65, 75),
               (85, 75), (85, 45), (95, 45)]

    force_diagram.create_polygon(points, outline="black", fill="red", width=2)
    force_diagram.create_polygon(
        points2, outline="black", fill="yellow", width=2)

    # Close
    def on_closing():
        if tkMessageBox.askokcancel("Quit", "Do you want to go back to Main Menu?"):
            back()
            clip2.stop()

    # Def Music On:
    def musicon():
        clip.play()
        music_on.config(state=DISABLED, fg="grey")
        music_off.config(state=NORMAL, fg="royalblue4")

    # Def Music Off:
    def musicoff():
        clip.stop()
        music_on.config(state=NORMAL, fg="royalblue4")
        music_off.config(state=DISABLED, fg="grey")

    global musicname, clip
    musicname = 'sounds/exciting.mp3'
    clip = mp3play.load(musicname)
    clip.play()
    root3.protocol("WM_DELETE_WINDOW", on_closing)

    # Def Help Button
    def helpme():
        global helproot
        try:
            helproot
        except NameError:
            helproot = methods.helpwindow(root3, 3)
        else:
            if helproot.winfo_exists() == 0:
                helproot = methods.helpwindow(root3, 3)
            else:
                helproot.deiconify()

    def reset_force():
        force_diagram.delete('all')
        points = [(75, 135), (55, 105), (65, 105),
                  (65, 75), (85, 75), (85, 105), (95, 105)]
        points2 = [(75, 15), (55, 45), (65, 45), (65, 75),
                   (85, 75), (85, 45), (95, 45)]
        force_diagram.create_polygon(
            points, outline="black", fill="red", width=2)
        force_diagram.create_polygon(
            points2, outline="black", fill="yellow", width=2)

    # reset
    def reset(rocket):
        global sky, land3, acceleration1, weight, position, people3, launchpad3, u, v, s, t, cover, cover_change, t
        t = 0
        t = 0
        u = 0
        v = 1
        s = 1
        position = [0,0, 0, 0]
        weight = 0
        weight_label.set(('Weight:', weight, 'N'))
        acceleration1 = 0
        acceleration.set(("Acceleration:", acceleration1, "ms^(-2)"))
        thrust_1.set(("Thrust:", thrust, "N"))
        animation.delete('all')
        land3 = animation.create_image(0, 430, anchor=SW, image=land1)
        sky = animation.create_image(0, -1400, anchor=NW, image=sky1_2)
        rockets = animation.create_image(150, 160, image=rocket)
        people3 = animation.create_image(-420, 125, anchor=NW, image=people)
        launchpad3 = animation.create_image(-230, -15,
                                            anchor=NW, image=launchpad1)
        reset_force()

    # move

    def move():
        global position, distance, t, cover, cover_change
        cover *= cover_change
        animation.move(land3, 0, cover)
        animation.move(launchpad3, 0, cover)
        animation.move(people3, 0, cover)
        animation.move(sky, 0, cover)
        time.sleep(t)
        animation.after(1, repeat)

    def repeat():
        global u, v, s, t, weight, acceleration1, force1, factor, cover_change
        position = animation.coords(sky)
        if position[1] > -10:
            clip2.stop()
            if str(music_on['state']) == 'disabled':
                clip.play()
            else:
                clip.stop()
            Back.config(state=NORMAL, bg='light blue2', fg='royalblue4')
            weight = 0
            scale['state'] = 'active'
            scale.set(0)
            scale['state'] = 'disabled'
            eight_instruction = "Congratulations! Your rocket has made it into space! Choose a new rocket to run the test again or go back to Main Menu to try out another Law. "
            typewriter(eight_instruction, 15)
            rocket1.config(state=NORMAL, bg='steel blue', fg='white')
            rocket2.config(state=NORMAL, bg='steel blue', fg='white')
            rocket3.config(state=NORMAL, bg='steel blue', fg='white')

        else:
            t *= 0.99
            animation.after(1, move)

    # Thrust
    def up(value=None):
        global acceleration1, weight, t, force1, factor, mass, cover_change
        if weight > 0:
            Back['state'] = 'disabled'
            rocket1['state'] = 'disabled'
            rocket2['state'] = 'disabled'
            rocket3['state'] = 'disabled'
            fire3 = animation.create_image(fire_coords, 270, image=fire2)
            force1 = scale.get()
            force1 = round(force1, 2)
            force2 = float(weight)
            thrust_1.set(("Thrust:", str(force1), "N"))
            force1 = int(force1)
            force3 = force1 - force2
            acceleration1 = force3 / mass
            acceleration1 = round(acceleration1, 3)
            factor = (force1 - weight) * 0.0001
            forces()
            if force3 > 0:
                cover_change += factor
                acceleration.set(("Acceleration:", acceleration1, "ms^(-2)"))
                scale['state'] = 'disabled'
                clip.stop()
                clip2.play()
                repeat()

            else:
                return None

    # Rockets
    def rocket1mass():
        global weight, mass, rocket1_3, fire_coords, cover, cover_change, t
        fire_coords = 150
        mass = 10
        Label(root3, text=('Mass:', mass, 'kg'), bg='royalblue4', fg='white', font=(
            "Comic Sans MS", 12)).place(relx=0.1, rely=0.76, anchor=CENTER)
        reset(rocket1_2)
        weight = 98.10
        weight_label.set(('Weight:', weight, 'N'))
        scale['state'] = 'active'
        t = 0.01
        cover_change = 1.009
        cover = 0.5

    def rocket2mass():
        global weight, mass, fire_coords, cover, cover_change, t
        mass = 20
        fire_coords = 140
        Label(root3, text=('Mass:', mass, 'kg'), bg='royalblue4', fg='white', font=(
            "Comic Sans MS", 12)).place(relx=0.1, rely=0.76, anchor=CENTER)
        reset(rocket2_2)
        weight = 196.2
        weight_label.set(('Weight:', weight, 'N'))
        scale['state'] = 'active'
        t = 0.02
        cover_change = 1.0085
        cover = 0.4

    def rocket3mass():
        global weight, mass, fire_coords, cover, cover_change, t
        fire_coords = 146
        mass = 30
        Label(root3, text=('Mass:', mass, 'kg'), bg='royalblue4', fg='white', font=(
            "Comic Sans MS", 12)).place(relx=0.1, rely=0.76, anchor=CENTER)
        reset(rocket3_2)
        weight = 294.3
        weight_label.set(('Weight:', weight, 'N'))
        scale['state'] = 'active'
        t = 0.03
        cover_change = 1.008
        cover = 0.3

    # Force Diagram
    def forces():
        global weight
        force_diagram.delete('all')
        points = [75, 135, 55, 105, 65, 105, 65, 75, 85, 75, 85, 105, 95, 105]
        force_diagram.create_polygon(
            points, outline="black", fill="red", width=2)
        change = scale.get()
        change = round(change, 2)
        x = 10 * (change / weight)
        if x > 10:
            x = 12
            points3 = [(75, 75 - 6 * x), (75 - 2 * x, 75 - 3 * x), (75 - x, 75 - 3 * x),
                       (75 - x, 75), (75 + x, 75), (75 + x, 75 - 3 * x), (75 + 2 * x, 75 - 3 * x)]
            force_diagram.create_polygon(
                points3, outline="black", fill="green", width=2)
        else:
            points2 = [(75, 15 + 6 * x), (55 + 2 * x, 45 + 3 * x), (65 + x, 45 + 3 * x),
                       (65 + x, 75), (85 - x, 75), (85 - x, 45 + 3 * x), (95 - 2 * x, 45 + 3 * x)]
            force_diagram.create_polygon(
                points2, outline="black", fill="yellow", width=2)
            points3 = [(75, 75 - 6 * x), (75 - 2 * x, 75 - 3 * x), (75 - x, 75 - 3 * x),
                       (75 - x, 75), (75 + x, 75), (75 + x, 75 - 3 * x), (75 + 2 * x, 75 - 3 * x)]
            force_diagram.create_polygon(
                points3, outline="black", fill="green", width=2)

    # Questions
    def gravity():
        global helproot1
        try:
            helproot1
        except NameError:
            helproot1 = methods.helpwindow(root3, 6)
        else:
            if helproot1.winfo_exists() == 0:
                helproot1 = methods.helpwindow(root3, 6)
            else:
                helproot1.deiconify()
            try:
                helproot2
            except NameError:
                pass
            else:
                helproot2.destroy()

    def calc_acceleration():
        global helproot2
        try:
            helproot2
        except NameError:
            helproot2 = methods.helpwindow(root3, 7)
        else:
            if helproot2.winfo_exists() == 0:
                helproot2 = methods.helpwindow(root3, 7)
            else:
                helproot2.deiconify()
            try:
                helproot1
            except NameError:
                pass
            else:
                helproot1.destroy()

    # Widgets
    # Title
    title = Label(frame_title, text="NEWTON'S THIRD LAW OF MOTION", fg='white', width=32,
                  relief=SUNKEN, font=("Comic Sans MS bold", 16),  bd=5, bg='royalblue4')
    title.place(relx=0.45, rely=0.05, anchor=CENTER)

    title = Label(frame_title, text="Theory: For every action, there is an equal and opposite reaction", relief=SUNKEN, fg='white', bg='royalblue4',
                  font=("Comic Sans MS", 12), wraplength=900, bd=5)
    title.place(relx=0.45, rely=0.115, anchor=CENTER)

    # Scale
    scale = Scale(frame_scale, from_=500, to_=0, width=150, length=300, command=up, repeatdelay=1090, resolution=10, bg='dodger blue3', fg='yellow2',
                  font='castellar 12 bold', activebackground='blue4', troughcolor='royal blue3', highlightbackground='cyan', sliderlength=50, state='disabled')
    scale.pack(expand=True)

    # Information
    Label(root3, text=('Mass:', mass, 'kg'), bg='royalblue4', fg='white',
          font=("Comic Sans MS", 12)).place(relx=0.1, rely=0.76, anchor=CENTER)

    weight_label = StringVar()
    weight_label.set(('Weight:', weight, 'N'))
    Label(root3, textvariable=(weight_label), bg='royalblue4', fg='white', font=(
        "Comic Sans MS", 12)).place(relx=0.1, rely=0.815, anchor=CENTER)

    thrust_1 = StringVar()
    thrust_1.set(("Thrust:", thrust, "N"))
    thrust_2 = Label(root3, textvariable=thrust_1,
                     bg='royalblue4', fg='white', font=("Comic Sans MS", 12))
    thrust_2.place(relx=0.4, rely=0.76, anchor=CENTER)

    acceleration = StringVar()
    acceleration.set(("Acceleration:", acceleration1, "ms^(-2)"))
    A = Label(root3, textvariable=acceleration, bg='royalblue4',
              fg='white', font=("Comic Sans MS", 12))
    A.place(relx=0.38, rely=0.815, anchor=CENTER)

    Label(root3, text="Weight", relief='ridge',
          bd=5, bg='red').place(x=590, y=580)
    Label(root3, text="Normal \nForce", relief='ridge',
          bd=5, bg='yellow').place(x=590, y=530)
    Label(root3, text="Upwards \nForce", relief='ridge',
          bd=5, bg='green').place(x=590, y=480)

    Label(root3, text="Thrust (N)", font='castellar 12 bold',
          relief='ridge', bd=5, bg='lightblue1').place(x=460, y=115)
    music_label = Label(frame_title, text="Music Status:", font=("Comic Sans MS", 11),
                        fg="white", bg="royalblue4", bd=5, height=1)
    music_label.place(relx=0.070, rely=0.025, anchor=CENTER)

    # Buttons
    rocket1 = Button(root3, text="Rocket 1", command=rocket1mass,
                     bd=5, bg='steel blue', fg='grey', font=("Comic Sans MS", 11), state='disabled')
    rocket1.place(x=20, y=590)

    rocket2 = Button(root3, text="Rocket 2", command=rocket2mass,
                     bd=5, bg='steel blue', fg='grey', font=("Comic Sans MS", 11), state='disabled')
    rocket2.place(x=120, y=590)

    rocket3 = Button(root3, text="Rocket 3", command=rocket3mass,
                     bd=5, bg='steel blue', fg='grey', font=("Comic Sans MS", 11), state='disabled')
    rocket3.place(x=220, y=590)

    Explaination1 = Button(root3, text="?", font=(
        "castellar 12 bold", 10), bg='royalblue4', fg='white', command=gravity, bd=3)
    Explaination1.place(relx=0.21, rely=0.815, anchor=CENTER)

    Explaination2 = Button(root3, text="?", font=(
        "castellar 12 bold", 10), bg='royalblue4', fg='white', command=calc_acceleration, bd=3)
    Explaination2.place(relx=0.55, rely=0.815, anchor=CENTER)

    Help = Button(frame_title, text="Help", relief=RAISED,
                  font=("Comic Sans MS", 12), fg='royalblue4',
                  bg="lightblue2", bd=5, command=helpme)
    Help.place(relx=0.8, rely=0.05, anchor=CENTER)

    music_on = Button(frame_title, text="ON", command=musicon, width=4,
                      font=("Comic Sans MS bold", 8), relief=RAISED,
                      fg='royalblue4', bg="lightblue2", bd=3, state="disabled")
    music_on.place(relx=0.032, rely=0.07, anchor=CENTER)

    music_off = Button(frame_title, text="OFF", command=musicoff, width=5,
                       font=("Comic Sans MS bold", 8), relief=RAISED,
                       fg='royalblue4', bg="lightblue2", bd=3)
    music_off.place(relx=0.098, rely=0.07, anchor=CENTER)

    def check_helproots(helproot):
        try:
            helproot
        except NameError:
            helproot_exists = False
        else:
            helproot_exists = True

    def back():
        typing_clip.stop()
        clip.stop()
        try:
            helproot
        except NameError:
            helproot_exists = False
        else:
            helproot_exists = True

        try:
            helproot1
        except NameError:
            helproot1_exists = False
        else:
            helproot1_exists = True

        try:
            helproot2
        except NameError:
            helproot2_exists = False
        else:
            helproot2_exists = True

        if helproot_exists:
            helproot.destroy()
        if helproot1_exists:
            helproot1.destroy()
        if helproot2_exists:
            helproot2.destroy()

        root3.destroy()
        main_window.deiconify()
        methods.type(main_window, menuclip, typing_clip, music_playing)

    Back = Button(frame_title, text="Main Menu", relief=RAISED,
                  font=("Comic Sans MS", 12), fg='royalblue4',
                  bg="lightblue2", bd=5, command=back)
    Back.place(relx=0.92, rely=0.05, anchor=CENTER)

    # Messages
    first_instruction = "Newton's Third Law of Motion states that for every action, there will be an equal opposite reaction."
    typewriter(first_instruction, 30)
    waitforcontinue()

    second_instruction = "A stationary rocket has its weight equal to the normal reaction force."
    typewriter(second_instruction, 30)
    waitforcontinue()

    third_instruction = "When the rocket's boosters are ignited, thrust pushes fuel downwards. The fuel produces an equal and opposite force pushing the rocket upwards."
    typewriter(third_instruction, 30)
    waitforcontinue()

    fourth_instruction = "This balance of Forces is illustrated in the Force Diagram on the right."
    typewriter(fourth_instruction, 30)
    waitforcontinue()

    fifth_instruction = "Click the help button for further assistance. All the best on exploring!!"
    typewriter(fifth_instruction, 30)
    waitforcontinue()

    rocket1.config(state=NORMAL, bg='steel blue', fg='white')
    rocket2.config(state=NORMAL, bg='steel blue', fg='white')
    rocket3.config(state=NORMAL, bg='steel blue', fg='white')

    root3.mainloop()
