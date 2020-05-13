# -*- coding: cp1252 -*-
from Tkinter import *
from PIL import Image, ImageTk
import tkMessageBox
import pygame
import os
import time
import mp3play
import methods
import pdb


class Rock(pygame.sprite.Sprite):

    def __init__(self, image):
        super(Rock, self).__init__()
        self.image = image
        self.rect = image.get_rect()
        self.x = 0.0
        self.y = 0.0
        self.movex = 0.0
        self.movey = 0.0
        self.angle = 0.0
        self.angle = 0.0

    def update(self, turn):
        self.angle = turn
        self.x += self.movex
        self.rect.centerx = self.x
        self.y += self.movey
        self.rect.centery = self.y

    def refresh(self):
        self.x = self.rect.centerx
        self.y = self.rect.centery


def Newtons_First_Law(main_window, menuclip, typing_clip, music_playing):

    global clip, musicname, helproot_exist
    root = Toplevel()
    methods.centralise(root, 950, 600)
    root.resizable(0, 0)
    root.title("NEWTON'S FIRST LAW OF MOTION")
    root.iconbitmap("images/newticon.ico")
    musicname = 'sounds/ambient.mp3'
    clip = mp3play.load(musicname)
    clip2 = mp3play.load('sounds/meteor.mp3')
    clip.play()
    # Ask User whether wants to exit or not

    def on_closing():
        if tkMessageBox.askokcancel("Quit", "Do you want to go back to Main Menu?"):
            back()
    root.protocol("WM_DELETE_WINDOW", on_closing)

    #() Animation Frame
    container = Frame(root, bg='royalblue4')
    container.pack(side=TOP, fill="both", expand=True)

    #(1) Button Frame
    buttonframe = Frame(root, height=34, bg='royalblue4')
    buttonframe.pack(side=BOTTOM, fill="both", expand=False)

    #(3) Pygame Frame
    pyg_width = 950
    half_pyg_width = pyg_width / 2
    pyg_height = 400
    half_pyg_height = pyg_height / 2
    embed = Frame(root, width=500, height=200, bg='black')
    embed.pack(expand=True, fill=BOTH)

    root.update()

    # insert pygame into Pygame Frame
    os.environ['SDL_WINDOWID'] = str(embed.winfo_id())

    if sys.platform == "win32":
        os.environ['SDL_VIDEODRIVER'] = 'windib'

    pygame.display.init()

    screen = pygame.display.set_mode((pyg_width, pyg_height))
    space = pygame.image.load('images/space1.gif')

    # placing big rock
    image = pygame.image.load('images/big_meteor.png')
    image = pygame.transform.scale(image, (70, 95))
    big_rock = Rock(image)

    # placing small rock
    image = pygame.image.load('images/big_meteor.png')
    image = pygame.transform.scale(image, (35, 47))
    image = pygame.transform.rotate(image, -85)
    small_rock = Rock(image)

    clock = pygame.time.Clock()
    fps = 60

    def move_for_collision():
        anime_button.config(state=DISABLED, fg="grey", bg="lightblue2")
        reset_button.config(state=DISABLED, fg="grey", bg="lightblue2")
        pop_up = "Let us assume the big meteor is stationary, and the small meteor is going to exert an external force on it."
        typewriter(pop_up, 30)
        waitforcontinue()
        new_button.destroy()
        colliding = True
        stepx = (big_rock.rect.centerx - small_rock.rect.centerx) / 60
        stepy = (big_rock.rect.centery - small_rock.rect.centery) / 60

        stepx *= 0.2
        stepy *= 0.3
        reversestepx = stepx * 0.5
        reversestepy = stepy * 0.0
        bigstepx = stepx * 0.45
        bigstepy = stepy * 0.35
        n = 1
        smallturn = 0.0
        bigturn = 0.0
        big_rock.refresh()
        small_rock.refresh()
        new_rect = small_rock.rect.copy()
        while colliding:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    colliding = False
                    after_collision = False
            if pygame.sprite.collide_rect(small_rock, big_rock):
                colliding = False
                after_collision = True
                clip2.play()
            if (small_rock.rect.centerx > big_rock.rect.centerx / 2) and (n < 2):
                typing_clip.stop()
                pop_up2 = "Once an external force is exerted on the big stationary meteor, it moves. "
                typewriter(pop_up2, 30)
                waitforcontinue()
                n += 1
            small_rock.movex = stepx
            small_rock.movey = stepy
            smallturn -= 0.3
            small_rock.update(smallturn)
            screen.blit(space, [0, -500])
            screen.blit(big_rock.image, big_rock.rect)
            small_rock_turned = pygame.transform.rotate(
                small_rock.image, small_rock.angle)
            screen.blit(small_rock_turned, small_rock.rect)
            clock.tick(fps)
            pygame.display.update()

        while after_collision:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    colliding = False
                    after_collision = False
            if big_rock.rect.centerx > pyg_width:
                after_collision = False
            small_rock.movex = -reversestepx
            small_rock.movey = -reversestepy
            smallturn -= 0.07
            small_rock.update(smallturn)
            big_rock.movex = bigstepx
            big_rock.movey = bigstepy
            bigturn -= 0.06
            big_rock.update(bigturn)
            screen.blit(space, [0, -500])
            small_rock_turned = pygame.transform.rotate(
                small_rock.image, small_rock.angle)
            screen.blit(small_rock_turned, small_rock.rect)
            big_rock_turned = pygame.transform.rotate(
                big_rock.image, big_rock.angle)
            screen.blit(big_rock_turned, big_rock.rect)
            clock.tick(fps)
            pygame.display.update()

        reset_button.config(state=NORMAL, fg="white", bg="royalblue4")
        anime_button.config(state=DISABLED, fg="grey", bg="lightblue2")

    def reset():
        reset_button.config(state=DISABLED, fg="grey", bg="lightblue2")
        screen.blit(space, [0, -500])

        big_rock.rect.centerx = half_pyg_width
        big_rock.rect.centery = half_pyg_height
        screen.blit(big_rock.image, big_rock.rect)

        small_rock.rect.centerx = 100
        small_rock.rect.centery = 100
        screen.blit(small_rock.image, small_rock.rect)

        anime_button.config(state=NORMAL, fg="white", bg="royalblue4")
        pygame.display.update()

    anime_button = Button(buttonframe, text="Begin Animation", relief=RAISED,
                          font=("Comic Sans MS", 12), fg='royalblue4',
                          bg="lightblue2", bd=5,
                          height=1, command=move_for_collision)
    anime_button.pack(side=LEFT, fill=BOTH, expand=True)

    reset_button = Button(buttonframe, text="Reset", relief=RAISED,
                          font=("Comic Sans MS", 12), fg='royalblue4',
                          bg="lightblue2", bd=5, state='disabled',
                          height=1, command=reset)
    reset_button.pack(side=LEFT, fill=BOTH, expand=True)
    reset()

    # Def Main Menu Button

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
        root.destroy()
        main_window.deiconify()
        methods.type(main_window, menuclip, typing_clip, music_playing)

    # Def Help Button

    def helpme():
        global helproot
        try:
            helproot
        except NameError:
            helproot = methods.helpwindow(root, 1)
        else:
            if helproot.winfo_exists() == 0:
                helproot = methods.helpwindow(root, 1)
            else:
                helproot.deiconify()

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

    # #Buttons
    back_btn = Button(container, text="Main Menu", relief=RAISED,
                      font=("Comic Sans MS", 12), fg='royalblue4',
                      bg="lightblue2", bd=5, command=back)
    back_btn.place(relx=0.91, rely=0.22, anchor=CENTER)

    helpbut = Button(container, text="Help", relief=RAISED,
                     font=("Comic Sans MS", 12), fg='royalblue4',
                     bg="lightblue2", bd=5, command=helpme)
    helpbut.place(relx=0.81, rely=0.22, anchor=CENTER)

    music_on = Button(container, text="ON", command=musicon, width=4,
                      font=("Comic Sans MS bold", 10), relief=RAISED,
                      fg='royalblue4', bg="lightblue2", bd=3, state="disabled")
    music_on.place(relx=0.07, rely=0.31, anchor=CENTER)

    music_off = Button(container, text="OFF", command=musicoff, width=5,
                       font=("Comic Sans MS bold", 10), relief=RAISED,
                       fg='royalblue4', bg="lightblue2", bd=3)
    music_off.place(relx=0.125, rely=0.31, anchor=CENTER)

    # Labels
    deftext = Label(root, text="Theory: An object will continue its state of motion (stationary/ constant velocity) unless an external force acts on it!",
                    relief=SUNKEN, fg='white', bg='royalblue4',
                    font=("Comic Sans MS", 12), wraplength=900, bd=5)
    deftext.place(relx=0.5, rely=0.155, anchor=CENTER)

    titletext = Label(root, text="NEWTON'S FIRST LAW OF MOTION", fg='white', width=32,
                      relief=SUNKEN, font=("Comic Sans MS bold", 20),  bd=5, bg='royalblue4')
    titletext.place(relx=0.475, rely=0.07, anchor=CENTER)

    music_label = Label(container, text="Music Status:", font=("Comic Sans MS", 11),
                        fg="white", bg="royalblue4", bd=5, height=1)
    music_label.place(relx=0.1, rely=0.13, anchor=CENTER)

    # Typewriter label
    message = Label(container, fg='white', font=("Comic Sans MS", 12), relief='ridge', bd=5,
                    bg='steelblue', text="", anchor=W, wraplength=700, justify=LEFT, width=79, height=2)
    message.place(relx=0.065, rely=0.66)

    def waitforcontinue():
        global new_button
        var = BooleanVar()
        new_button = Button(root, bd=5,
                            bg='royalblue4', fg='white', font=("Comic Sans MS", 12), text="Next",
                            command=lambda: var.set(True))
        new_button.place(relx=0.83, rely=0.205)
        new_button.wait_variable(var)
        new_button.destroy()

    def typewriter(text, delay):
        typing_clip.play()

        def wait():
            var = IntVar()
            root.after(delay, var.set, 1)
            root.wait_variable(var)
        message_text = text
        message_display = ""

        for letter in message_text:
            message_display += letter
            wait()
            message.configure(text=message_display)
        typing_clip.stop()

    counter = 0
    if counter == 0:
        # Typewriter
        reset_button.config(state=DISABLED, fg="grey", bg="lightblue2")
        anime_button.config(state=DISABLED, fg="grey", bg="lightblue2")
        pygame.display.update()
        first_instruction = "Hi, welcome to Newton's First Law of Motion, in this section, Newt will be guiding you through the definition of the First Law."
        typewriter(first_instruction, 30)
        waitforcontinue()
        pygame.display.update()

        second_instruction = "Isaac Newton states that an object will continue its state of motion unless a force acts on it."
        typewriter(second_instruction, 30)
        waitforcontinue()
        pygame.display.update()

        third_instruction = "Click the Begin Animation button to start."
        typewriter(third_instruction, 30)
        waitforcontinue()
        pygame.display.update()
        if big_rock.rect.centerx < pyg_width:
            reset_button.config(state=DISABLED, fg="grey", bg="lightblue2")
            anime_button.config(state=NORMAL, fg="white", bg="royalblue4")
        pygame.display.update()
        counter += 1

    root.mainloop()
