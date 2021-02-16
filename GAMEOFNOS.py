import random
import time
def loading () :
    time.sleep(1.5)
    print("Dice is being rolled ....")
    time.sleep(3)

def countdown () :
    print("Commencing Game in .....")
    for i in range(4) :
      print(4-i,"...",end="")
      time.sleep(1);




print("Welcome to *GAME OF NUMBERS*")
print("The rules are simple ..... :")
print("The person with the highest no. wins the game")
print("Menu :")
print("\t 1.Single player \n \t 2.Multiplayer")
i=int(input("Awaiting your command :"))
t=1
#while t>0 :
#    print("ROUND \t",t)
if i==1 :
    countdown()
    print("\n")
    print("Your Turn :")
    print("Roll dice ?[y/n]")
    var=input();
    if var=='y' :
      a=random.randint(1,6)
      loading()
      print("You got a ",a)
      time.sleep(2)
      print("Bot's turn :")
      c = random.randint(1,6)
      loading()
      print("The bot got a ", c)
      time.sleep(2)
      if a>c:
        print("You Win")
      if a<c :
        print("Sorry , The bot wins")
      if a==c :
        print("Its a draw")
    else:
        print("Okay then ......")
if i==2 :
    print("This feature is not yet available")
