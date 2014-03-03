#
#
# RUSSIAN ROULETTE (V2.2)
#
# MAX HAYES & ROYCE POPE
#
#ADD LATER:
#   -add sound with pygame
#   -add timing (don't know how)
#   -create rules for player names (cannot be blank, cannot be the same)
#   -create a widget-deleter class to clean up code for changing scenes
#
#######################################################################################################


#Imports libraries
from tkinter import *
import pygame
from random import randint

#INIT CLASSES:

class Gun: # Creates Gun class; methods for 'pulling trigger' and 'spinning'
    def __init__(self, capacity=7, bullet_pos = randint(1, 7), chamber_fired = randint (1,7)):
        self.capacity = capacity
        self.bullet_pos = bullet_pos
        self.chamber_fired = chamber_fired 
    def pull_trigger(self):
        if self.chamber_fired==self.bullet_pos:
            return(False)
        elif self.chamber_fired==7:
            self.chamber_fired=1
            return(True)
        else:
            self.chamber_fired+=1
            return(True)
    
    def spin(self):
        self.chamber_fired = randint (1,7)
        
                
class Player: # Creates Player class; method to contain # of spins each player (object) has used
    def __init__(self, name='xxx', spin_count=2):
        self.name=name
        self.spin_count=spin_count
    def spin(self):
        if self.spin_count > 0:
            self.spin_count-=1
            return(True)
        else:
            return(False)
    

#Defines Widget Functions:
def game_window():  # WIDGET LAYOUT FOR GAME
    text_instruct.grid_forget()
    p1_trigger.grid(row = 1, column = 1)
    spin_button.grid(row = 2, column = 1)

    global game_message 
    game_message = StringVar()
    game_label = Label(app, textvariable = game_message)
    game_label.grid(row = 0, column = 1)
    game_message.set("Your Turn, " + player_1.name)

    global spin_message
    spin_message = StringVar()
    spin_label = Label(app, textvariable = spin_message)
    spin_label.grid(row = 3, column = 1)
    spin_message.set("%s, you have %d spins left" % (player_1.name, player_1.spin_count))

def submit_push_1(): # Creates object for Player_1 with name entered
    global player_1
    p1_name = name_field.get()
    player_1 = Player(p1_name)
    name_field.delete(0, END)
    submit_button_1.grid_forget()
    submit_button_2.grid(row=3, column=0, padx=hpad)
    message.set("Enter the second player's name:")
    app.bind("<Return>", lambda event: submit_push_2())
        
def submit_push_2(): # Replaces the first button with an identical one and creates object for Player_2 with name entered
    global player_2
    p2_name = name_field.get()
    player_2 = Player(p2_name)    
    name_field.delete(0, END)
    submit_button_2.grid_forget()
    name_field.grid_forget()
    l1.grid_forget()
    global next_window
    next_window = True
    text_instruct.grid()
    app.bind("<Return>", lambda event: game_window())
    


#:::::::::::::::::::::::::::::::::::::::::::  G   U   I  ::::::::::::::::::::::::::::::::::::::::::::::

#ENTER NAMES WINDOW::::::::::::::::::::::::::::::::::::::::::::::
app = Tk()
app.title("RUSSIAN ROULETTE - enter names")
app.geometry('+600+300') #Geometry expands to fit whatever widgets are inside. the +600+300 are coordinates for screen placement.
#Enter Names Widget:

hpad = 40 # constant 'horizontal pad' for below widgets (so it can be quickly changed for all widgets)

#displays text on the screen
message=StringVar()
l1 = Label(app, textvariable=message)
l1.grid(row=1, column=0, padx=hpad)
message.set("Enter the first player's name:")

#entry field for name(s)
name_field = Entry(app)
name_field.grid(row=2, column = 0, padx=hpad)

# Creates new Player object with name taken from Entry widget
submit_button_1 = Button(app, width = 15, text = "Submit P1 Name", command = submit_push_1)
submit_button_1.grid(row=3, column=0, padx=hpad)
app.bind("<Return>", lambda event: submit_push_1()) #ENTER key = pressing 'submit_button'

#Button 2 is the same as button one, but calls a different function. There is probably a better way to do this...
submit_button_2 = Button(app, width = 15, text = "Submit P2 Name", command = submit_push_2)
submit_button_2.grid(row=3, column=0, padx=hpad)
submit_button_2.grid_forget()
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    

#INSTRUCTIONS WINDOW::::::::::::::::::::::::::::::::::::::::::::::::
def init_instructions(): # Is only a fuction so it can be collapsed in KOMODO EDIT
    global instructions
    instructions = '''::::::::::::::::::::::::::::::::::::::::::  INSTRUCTIONS  ::::::::::::::::::::::::::::::::::::::::::    
    You are about to play Russian Roulette.    

    The revolver holds 7 bullets.    

    The bullet starts out in a random position and the revolver is spun.    

    Each trigger pull takes you one step closer to the bullet position.    
    (Unless you spin the revolver; this randomizes the chamber to be fired.)    

    Each player gets 2 spins per game.    

    ::::::::::::::::::::::::::::::::::::::::::  HIT 'ENTER' TO BEGIN  :::::::::::::::::::::::::::::::::::::::::::    '''

init_instructions()
text_instruct = Label(app, text = instructions, wraplength='500')

# Game Runntime:
gun = Gun()
global alive
alive=True
global spinning
spinning=False


def spin():
    global spinning
    spinning = True
    print('spinning')

def result(name):
    print('''\nPLAYER: %s
BULLET: %d
CHAMBER: %d
:::::::::::::::::::::::::::\n
:::::::::::::::::::::::::::''' % (name, gun.bullet_pos, gun.chamber_fired))
    
    
def player_1_turn():
    game_message.set("Your turn, " + player_2.name)
    spin_message.set("%s, you have %d spins left" % (player_2.name, player_2.spin_count))
    global spinning
    global alive
    player = player_1.name
    if spinning == True: #Checks if the player wants to spin
        spinning = player_1.spin()
        if spinning == True:  #Checks to see if the player has spins left
            gun.spin()        #Randomizes chamber_fired value 
    alive = gun.pull_trigger() #pull trigger and returns 'True' if player lived
    p1_trigger.grid_forget()
    p2_trigger.grid(row = 1, column = 1)
    result(player_1.name) #Prints results in IDLE for diagnostics
    if alive!=True:  #If the player is not alive...
        p2_trigger.grid_forget()    #...remove all buttons...
        spin_button.grid_forget()
        spin_message.set('DX')
        game_message.set("YOU LOSE, %s!!!!" % player_1.name)     #...and tell them they lost.
    spinning = False
    spin_message.set(' ')


def player_2_turn():
    game_message.set("Your turn, " + player_1.name)
    spin_message.set("%s, you have %d spins left" % (player_1.name, player_1.spin_count))
    global spinning
    global alive
    player = player_1.name
    if spinning == True: #Checks if the player wants to spin
        spinning = player_2.spin()
        if spinning == True:  #Checks to see if the player has spins left
            gun.spin()        #Randomizes chamber_fired value 
    alive = gun.pull_trigger() #pull trigger and returns 'True' if player lived
    p2_trigger.grid_forget()
    p1_trigger.grid(row = 1, column = 1)
    result(player_2.name)  #Prints results in IDLE for diagnostics
    if alive!=True:    #If the player is not alive...  
        p1_trigger.grid_forget()#...remove all buttons...
        spin_button.grid_forget()
        spin_message.set('DX')
        game_message.set("YOU LOSE, %s!!!!" % player_2.name) #...and tell them they lost.
    spinning = False
    spin_message.set(' ')

#GAME WINDOW WIDGETS:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# "Pulls trigger" for the respective player
p1_trigger = Button(app, text = "Pull Trigger", command = player_1_turn)
p1_trigger.grid(row = 1, column = 1)
p1_trigger.grid_forget()
p2_trigger = Button(app, text = 'Pull Trigger', command = player_2_turn)
p2_trigger.grid(row = 1, column = 1)
p2_trigger.grid_forget()

# "Spins" for the respective player
spin_button=Button(app, text="spin revolver", command = spin)
spin_button.grid(row = 2, column = 1)
spin_button.grid_forget()


