from random import randint
import time

def show_dev_info():
    print("          :::DEV INFO:::")
    print("::: Bullet is in chamber number "+str(bullet) + ":::")
    print("::: Chamber number " + str(chamber) + " was fired: ::::")
    print("::::::::::::::::::::::::::::::::::::")
    time.sleep(1)
    print()
    print()


print("Would you and your friend like to play a game?")
a=input("Y/N?: ")
if a==("n"):
    print("Fine, you are boring")
else:
    print("The game is 'Russian 'Roulette.")
    time.sleep(1)
    print("I just have a couple questions...:")
    time.sleep(1)
    print()
    
    n=input("How many bullets can your gun hold?: ")
    number =int(n)
    time.sleep(float(.5))
    print("OK, your gun can hold " +str(number) +" bullets.")
    time.sleep(float(.5))
    print()

    
    print("'DEV MODE' displays 'bullet' value and 'chamber' value after each trigger pull.")
    time.sleep(float(2.5))
    print()
    d=input("Would you like to run program in 'DEV MODE?'(Y/N)?: ")
    dev=str(d)
    print()
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

    
    b =randint(1,number)
    bullet=int(b)
    t=randint(1,number)
    p =1
    player=int(p)
    
    while t!=bullet:
        input("Player " + str(player) + ": press 'ENTER' to pull the trigger::::::::::::::::")
        print()
        chamber= int(t)
        if chamber!=bullet:
            print("Hammer clicks back...")
            time.sleep(1)
            print("...")
            time.sleep(float(1.75))
            print()
            print("'*CLICK.*'")
            time.sleep(float(1.5))
            print()
            if dev==("y"):
                show_dev_info()
            if player==1:
                player+=1
            else:
                player-=1
            print("You are safe... for now")
            print()
            time.sleep(float(.5))
            print("::: Hand the gun to player " + str(player) + ":::")
            print()
            time.sleep(1)
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            if chamber==number:
                number-=1
                t-=number
            else:
                t+=1
    input("Player " + str(player) + " Press 'ENTER' to pull the trigger::::::::::::::::")
    print("Hammer clicks back...")
    time.sleep(1)
    print("...")
    time.sleep(float(2.5))
    print()
    print("BANG!!!")
    time.sleep(1)
    print("you lose, player " + str(player) +"!!!")
time.sleep(float(.5))
print("Game over")
print("::::::::::::::::::::::::::::::::::::::")
          
