from Tkinter import *
from PIL import Image, ImageTk
import tkMessageBox
import pygame
import os
import time
import mp3play
import methods


def Newtons_Second_Law(main_window, menuclip, typing_clip, music_playing):
    global tries, stick, ball, balls, clip, musicname
    tries = 1

    OFFWHITE = 'lemonchiffon'
    TEXTBROWS = 'saddlebrown'
    FONTFAMILY = "Comic Sans MS"

    root2 = Toplevel()
    methods.centralise(root2, 900, 600)
    root2.resizable(0, 0)
    root2.title("NEWTON'S SECOND LAW OF MOTION")
    root2.iconbitmap("images/newticon.ico")
    root2.configure(bg='royalblue4')
    musicname = 'sounds/cool.mp3'
    clip = mp3play.load(musicname)
    clip.play()

    def on_closing():
        if tkMessageBox.askokcancel("Quit", "Do you want to go back to Main Menu?"):
            back()
    root2.protocol("WM_DELETE_WINDOW", on_closing)

    def acceleration(F, f):
        global Force, friction
        Force = F
        friction = f
        F -= f
        acc = F / 0.16
        return acc

    def velocity(acc, t):
        v = acc * t
        return v

    def displacement(vel, acc, t):
        global decc, dist_1, dist_2, dist_2_time, total_dist
        dist_1 = (0.5) * (acc) * (t**2)
        decc = 2 / 0.16
        dist_2 = (-(vel**2)) / (2 * (-decc))
        dist_2_time = (-vel) / (-decc)
        total_dist = dist_1 + dist_2
        return total_dist

    def wait_for_continue():
        global new_button

        var = BooleanVar()
        new_button = Button(root2, bd=5,
                            bg='royalblue4', fg='white', font=("Comic Sans MS", 12), text="Next",
                            command=lambda: var.set(True))
        new_button.place(relx=0.876, rely=0.58)
        new_button.wait_variable(var)
        new_button.destroy()

    def explain():

        screen.blit(zoomed_expl, [0, 0])
        screen.blit(v_arrow, [450, 50])
        screen.blit(v_arrow, [500, 50])

        force = Forcefont.render('F = ' + str(Force) + 'N', True, (0, 0, 0))
        forceRect = force.get_rect()
        frictionfont = pygame.font.Font('images/ARLRDBD.ttf', 22)
        friction_text = frictionfont.render(
            'f = ' + str(friction) + 'N', True, (0, 0, 0))
        frictionRect = friction_text.get_rect()
        screen.blit(force, [450, 10])
        screen.blit(friction_text, [265, 103])
        screen.blit(f_arrow, [225, 110])
        pygame.display.update()
        instruction = "The Force applied by the Stick is " + str(Force) + "N. The friction is " + str(
            friction) + "N. Hence, the ball experiences a net forward Force of " + str(Force - friction) + "N."
        typewriter(instruction, 20)
        wait_for_continue()

        instruction = "The mass of the ball is 0.16kg. Obeying ' F = m x a ': The acceleration is " + \
            str(acc) + "ms^(-2). Here, the ball experiences this acceleration for 1 second."
        typewriter(instruction, 20)
        wait_for_continue()

        screen.blit(zoomed_expl, [0, 0])
        screen.blit(v_arrow, [450, 50])

        velfont = pygame.font.Font('images/ARLRDBD.ttf', 27)
        velocity_text = velfont.render(str(vel) + 'm/s', True, (0, 0, 0))
        screen.blit(velocity_text, [450, 10])
        pygame.display.update()
        instruction = "Hence, the ball will reach a max velocity of " + \
            str(vel) + "m/s after 1s. The ball will only experience friction after that causing it to decelerate to a stop."
        typewriter(instruction, 20)
        wait_for_continue()

    def game_balls():
        global balls, ball
        balls = []
        for n in [0, 1, 2, 3]:
            filename = 'images/ball' + str(n) + '.png'
            ball = pygame.image.load(filename)
            ball = pygame.transform.scale(ball, (25, 25))
            balls. append(ball)

    def game_stick():
        global stick
        stick = pygame.transform.scale(stick, (150, 52))

    def push(F, t, f):
        global tries, acc, vel, stick_x, stick_y, ball_x, ball_y, rect_first_boundary, rect_second_boundary
        start_button.config(state="disabled")
        acc = acceleration(F, f)
        vel = velocity(acc, t)
        total_dist = displacement(vel, acc, t)

        ball_x_change = 0

        if tries > 2:
            ball_x = 142
            ball_y = 123
            stick_x = -10
            stick_y = 107
        if tries <= 2:
            ball_x = 340
            ball_y = 98
            stick_x = 30
            stick_y = 50

        ball_n = 0
        fps = 60

        vel_x = Force * 0.99

        clock = pygame.time.Clock()

        accelerating = False
        decelerating = False

        if tries == 1:
            explain()

        accelerating = True

        rect_first_boundary = 600
        rect_second_boundary = 650

        rotation = 0
        rotation_amt = 0

        start_button.config(state="disabled")

        while accelerating:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    accelerating = False

            if ball_x_change > vel_x:
                accelerating = False
                decelerating = True

            junglebackground()
            grassbackground()
            if tries >= 3:
                pygame.draw.rect(screen, (225, 0, 0),
                                 (rect_second_boundary, 148, 10, 40))
                pygame.draw.rect(screen, (225, 0, 0),
                                 (rect_first_boundary, 148, 10, 40))

            poolstick(stick_x, stick_y)
            ballimage(ball_n, ball_x, ball_y)

            if ball_x_change == 0:
                ball_x_change += 0.5

            ball_x_change = ball_x_change / 0.92
            ball_x += ball_x_change
            rotation += 0.025
            ball_n += rotation

            if ball_n > 3:
                ball_n = 0

            stick_x += ball_x_change

            clock.tick(fps)
            pygame.display.update()

        while decelerating:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    accelerating = False

            if ball_x_change <= 0.1:
                decelerating = False

            junglebackground()
            grassbackground()
            poolstick(stick_x, stick_y)
            ballimage(ball_n, ball_x, ball_y)
            if tries >= 3:
                pygame.draw.rect(screen, (225, 0, 0),
                                 (rect_first_boundary, 148, 10, 40))
                pygame.draw.rect(screen, (225, 0, 0),
                                 (rect_second_boundary, 148, 10, 40))


            ball_x_change *= 0.95
            ball_x += ball_x_change

            rotation *= 0.97
            ball_n += rotation
            if ball_n > 3:
                ball_n = 0

            clock.tick(fps)
            pygame.display.update()

            if ball_x > 800:
                decelerating = False

        tries += 1

        if tries == 2:
            instruction = "Try a different magnitude of Force!"
            typewriter(instruction, 20)
            start_button.config(state=NORMAL, bg='steel blue', fg='white')
        elif tries == 3:
            reset()
            pygame.draw.rect(screen, (225, 0, 0), (600, 148, 10, 40))
            pygame.draw.rect(screen, (225, 0, 0), (650, 148, 10, 40))
            pygame.display.update()
            force_scale.config(from_=17, to_=3)
            instruction = "You got the hang of it! Now try to stop the ball between the red lines."
            typewriter(instruction, 20)
            start_button.config(state=NORMAL, bg='steel blue', fg='white')

        else:
            checkwin()
            start_button.config(state=NORMAL, bg='steel blue', fg='white')

    def reset():
        ball_x = 142
        ball_y = 123
        stick_x = -10
        stick_y = 107
        junglebackground()
        grassbackground()
        game_balls()
        ballimage(0, 142, 123)
        game_stick()
        poolstick(-10, 107)

    def checkwin():
        
        if ball_x > rect_first_boundary and ball_x < rect_second_boundary:
            instruction = "   Well Played!!"
            typewriter(instruction, 20)
        else:
            instruction = "Failure is the pillar of success! Try again :)"
            typewriter(instruction, 20)

    def junglebackground():
        screen.blit(jungle, [-1100, -620])

    def grassbackground():
        screen.blit(grass, [0, -400])

    def poolstick(x, y):
        stickRect = pygame.Rect((x, y), (300, 107))
        screen.blit(stick, stickRect)

    def ballimage(number, x, y):
        new_ball = balls[int(number)]
        ballRect = pygame.Rect((x, y), (50, 50))
        screen.blit(new_ball, ballRect)

    def back():
        pygame.display.quit()
        typing_clip.stop()
        clip.stop()
        try:
            helproot
        except NameError:
            helproot_exists = False
        else:
            helproot_exists = True

        if helproot_exists:
            helproot.destroy()
        root2.destroy()
        main_window.deiconify()
        methods.type(main_window, menuclip, typing_clip, music_playing)

    def formula():
        tkMessageBox.showinfo(
            'Formulas used:', 'F = m x a\nv = a *t\nv**2 = u**2 + 2as', parent=root2)

    def helpme():
        global helproot
        try:
            helproot
        except NameError:
            helproot = methods.helpwindow(root2, 2)
        else:
            if helproot.winfo_exists() == 0:
                helproot = methods.helpwindow(root2, 2)
            else:
                helproot.deiconify()

    titletext = Label(root2, text="NEWTON'S SECOND LAW OF MOTION",
                      fg='white', width=33, relief=SUNKEN,
                      font=("Comic Sans MS bold", 20),  bd=5, bg='royalblue4')
    titletext.place(relx=0.475, rely=0.07, anchor=CENTER)
    deftext = Label(root2, text="Theory: The second law states that acceleration of an object is dependent upon two variables - the net force acting upon the object and its mass.",
                    relief=SUNKEN, fg='white', bg='royalblue4', font=("Comic Sans MS", 12), wraplength=900, bd=5)
    deftext.place(relx=0.5, rely=0.19, anchor=CENTER)

    # new frame for pygame
    pyg_width = 800
    half_pyg_width = pyg_width / 2
    pyg_height = 200
    half_pyg_height = pyg_height / 2
    embed = Frame(root2, width=pyg_width, height=pyg_height,
                  background="white", highlightbackground="black", highlightthickness=3)
    embed.place(relx=0.5, rely=0.28, anchor=N)
    root2.update()

    # insert pygame into tkinter frame
    os.environ['SDL_WINDOWID'] = str(embed.winfo_id())

    if sys.platform == "win32":
        os.environ['SDL_VIDEODRIVER'] = 'windib'

    pygame.display.init()

    screen = pygame.display.set_mode((pyg_width, pyg_height))
    jungle = pygame.image.load('images/jungle.png')
    jungle = pygame.transform.rotate(jungle, -5.0)
    grass = pygame.image.load('images/green-grass.png')
    grass = pygame.transform.scale(grass, (800, 800))
    stick = pygame.image.load('images/poolstick.png')
    stick = pygame.transform.scale(stick, (300, 107))
    stick = pygame.transform.rotate(stick, -7.5)
    zoomed_expl = pygame.image.load('images/zoomedball.jpeg')
    f_arrow = pygame.image.load('images/f_arrow.png')
    f_arrow = pygame.transform.scale(f_arrow, (120, 40))
    small_f_arrow = pygame.transform.scale(f_arrow, (60, 20))
    v_arrow = pygame.image.load('images/v_arrow.png')
    v_arrow = pygame.transform.scale(v_arrow, (63, 98))
    small_v_arrow = pygame.transform.scale(v_arrow, (21, 31))

    pygame.font.init()

    Forcefont = pygame.font.Font('images/ARLRDBD.ttf', 32)
    force = Forcefont.render('F = 10N', True, (0, 0, 0))
    forceRect = force.get_rect()
    frictionfont = pygame.font.Font('images/ARLRDBD.ttf', 22)
    friction_text = frictionfont.render('f = 2N', True, (0, 0, 0))
    frictionRect = friction_text.get_rect()

    # screen.blit(screenshot, [-100, -100])

    balls = []
    for n in [0, 1, 2, 3]:
        filename = 'images/'+'ball' + str(n) + '.png'
        ball = pygame.image.load(filename)
        ball = pygame.transform.scale(ball, (50, 50))
        balls. append(ball)

    # insert jungle background
    junglebackground()

    # insert grass image
    grassbackground()

    # insert poolstick image
    poolstick(30, 50)
    # poolstick(-10, 100)

    # insert ball image
    ballimage(0, 340, 98)
    # ballimage(0, 142, 123)

    velfont = pygame.font.Font('images/ARLRDBD.ttf', 27)
    velocity_text = velfont.render('30m/s', True, (0, 0, 0))

    pygame.display.update()

    force_label = Label(root2, text="Force (N):", bg='royalblue4',
                        fg='white', font=("Comic Sans MS", 13))
    force_label.place(relx=0.258, rely=0.73, anchor=CENTER)
    force_scale = Scale(root2, from_=10, to_=5, width=50, length=100,
                        repeatdelay=1000, resolution=1, sliderlength=50, bg='royalblue4', fg='white', font=("Comic Sans MS", 12))
    force_scale.place(relx=0.25, rely=0.76, anchor=N)
   
    helpbut = Button(root2, text="Help", relief=RAISED,
                     font=("Comic Sans MS", 12), fg='royalblue4',
                     bg="lightblue2", bd=5, command=helpme)
    helpbut.place(relx=0.84, rely=0.07, anchor=CENTER)

    back_btn = Button(root2, text="Main Menu", relief=RAISED,
                      font=("Comic Sans MS", 12), fg='royalblue4',
                      bg="lightblue2", bd=5, command=back)
    back_btn.place(relx=0.94, rely=0.07, anchor=CENTER)

    message = Label(root2, fg='white', font=("Comic Sans MS", 12), relief='ridge', bd=5,
                    bg='steel blue', text="", anchor=W, wraplength=700, justify=LEFT, width=79, height=2)
    message.place(relx=0.5, rely=0.57, anchor=N)

    def typewriter(text, delay):
        typing_clip.play()

        def wait():
            var = IntVar()
            root2.after(delay, var.set, 1)
            root2.wait_variable(var)
        message_text = text
        message_display = ""
        
        for letter in message_text:
            message_display += letter
            wait()
            message.configure(text=message_display)
        typing_clip.stop()

    # background music
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

    music_on = Button(root2, text="ON", command=musicon, width=4,
                      font=("Comic Sans MS bold", 10), relief=RAISED,
                      fg='royalblue4', bg="lightblue2", bd=3, state="disabled")
    music_on.place(relx=0.045, rely=0.095, anchor=CENTER)

    music_off = Button(root2, text="OFF", command=musicoff, width=5,
                       font=("Comic Sans MS bold", 10), relief=RAISED,
                       fg='royalblue4', bg="lightblue2", bd=3)
    music_off.place(relx=0.105, rely=0.095, anchor=CENTER)

    music_label = Label(root2, text="Music Status:", font=("Comic Sans MS", 11),
                        fg="white", bg="royalblue4", bd=5, height=1)
    music_label.place(relx=0.075, rely=0.04, anchor=CENTER)

    start_button = Button(root2, text="Start", command=lambda: push(
        force_scale.get(), 1, 2), bd=5, bg='steel blue', fg='white', font=("Comic Sans MS", 16), width=10)

    start_button.place(relx=0.65, rely=0.85, anchor=CENTER)

    # Ask User whether wants to exit or not

    first_instruction = "Please choose the magnitude of Force you wish to apply on the ball and click Start"

    typewriter(first_instruction, 20)

    root2.mainloop()
