import time
import os
import _ctypes
import random
Squad={}
stack=[]
import winsound
def playintro() :
        winsound.PlaySound('Gravity falls game song',winsound.SND_ASYNC)
        time.sleep(19)
        winsound.PlaySound(None,winsound.SND_ASYNC)


#def warning(i) :
#    print("Do you confirm the action below (y/n)?")
#    ans=input()
#    if ans=='y' :
#        print('Okay then ,')
#
#    if ans=='n' :
#        i=input("Choose any Action[1,2,3,4] :")
#        return(i)



def countdown(t) :
    i=0
    print("Loading ,Please wait ",end=' ')
    while i<=t :
        print(t-i,"...",end='\r')
        time.sleep(1)
        i+=1


def sounds(s) :
    t=0
    if s=='walk':
        while t<3 :
            print("Thomp . . .",end="")
            time.sleep(1)
            t+=1
    if s=='run' :
        while t<4 :
            print("Thomp . . .",end="")
            time.sleep(0.5)
            t+=1
    if s=='crawl':
        while t<3 :
            print("shk shk . . .",end="")
            time.sleep(1)
            t+=1
def endings (bonus_points ,punish) :
    return(bonus_points + punish)

#class stats :
#    def __init__(self, name ,w1,w2,w3,w4,w5):   #w1 ,w2 and all are no.of times the weapon is used
#        self.name = name;
#        self.w1 = w1
#        self.w2 = w2
#        self.w3 = w3
#        self.w4 = w4
#        self.w5 = w5
def savegame(Gamer_name,savepoint=00) :
    k=0
    Gamer_temp=Gamer_name
    fin=open('Gamers.txt',mode='rt')
    Gamers=[]
    Gamers=fin.read()
    c=str(savepoint)
    Gamer_temp+=c                     ## Maximum 99 decisions
    while k>=0:
        if _ctypes.sizeof(Gamers[k])>=_ctypes.sizeof(Gamer_name) :
            if abs(Gamer_name - Gamers[k]) >= 48 * 2 and abs(Gamer_name - Gamers[k]) <= 57 * 2:
                Gamers.replace(Gamers[k],Gamer_temp)
        k+=1                     ## else part not required coz newgame does the job
    fout=open('Gamers.txt',mode='w')
    s=0
    while s<k :
        fout.write(Gamers[s])
        fout.write('\n')
        s+=1




def Newgamesave (Gamer_name) : #needs work
    i = 1
    s=0
    while i > 0:
        d = Gamer_name
        d+='00'                                         ##Future Tabish remember choices should be 99 Max
        stack.append(d)
        print("DO YOU WISH TO CONTINUE ?[5 for exit,0 for continue]")
        s = int(input())
        if s == 5:
            break
        i += 1
    j = 0
    f = open("Gamers.txt", "w")
    while j < i:
        o = stack[j]
        f.write(o)
        f.write("\n")
        j += 1
    f.close()
    del stack
    fin=open("TRACKHACK.txt",'r')
    fin.truncate(0)
    fin.close()


def detector(Name_size,charsize) :
    i=0
    s=0
    while Name_size[i] !=None :
        if Name_size[i]>=48 and Name_size[i]<=57 :
            s=s*10+Name_size[i];
        i+=1
    charsize=s


def Countinue(Gamer_name,savepoint) :
    q=0
    f1 = open("Gamers.txt", "r")
    Names=[]
    if f1.mode == "r":
        Names = f1.read()
        print(Names)
    f1.close()
    while q>=0 and i==0:
       a = Names[q]
       if _ctypes.sizeof(a)>=_ctypes.sizeof(Gamer_name) :
          if abs(Gamer_name-a)>=48*2 and abs(Gamer_name-a)<=57*2 :
               detector(a,savepoint)
       q+=1
    savegame(Gamer_name,savepoint)
    print("Game Saving")
    countdown(3)



#PartyPACK
def squadprint(Squad) :
    if Squad ==None :
        print('No one is in the party')
    else :
        k=1
        print('Party Updated')
        while k<=5:
            a=Squad.get(k)
            print('\t',Squad[k] ,'\t joined the party')
            k+=1
            time.sleep(1.4)




#START OF PLOTs
def s1_1(Gamer_name) :
    time.sleep(1)
    print('Our hero',Gamer_name,' stands up and walks towards his comrades')
    time.sleep(1.26)
    sounds('walk')
    print('He salutes his commander and debriefs for their plan of attack')
    print('"We plan to land on our remote safe house 2 km away from the Vietnamese Military base", says Zammy')
    print('Commander Kantshri Matmann orders the hero\'s strike team to attack the Vietnam military base at Lu Doan 206')
    print('Your squad that includes :',end=' ')
    print(Gamer_name,' ,Zammy ,Captain Gru McFallow ,Sanjay ,Akshay and Private Ayush')
    Squad={1:'Zammy 1',2:'Captain Gru McFallow 1',3:'Sanjay 1',4:'Akshay 1',5:'Ayush 1'}
    squadprint(Squad)


def s1_2(Gamer_name) :
    print(Gamer_name, "decides to walk towards the cockpit before going on the mission")
    time.sleep(1.5)
    sounds('walk')
    print('As ',Gamer_name,' enters , he finds the pilot was subdued laying on the ground and decided to proceed',end='')
    print('with caution')
    print('Choose method :')
    print("1.Crawl \t 2. Slow walk \n 3. Confront \t 4.Wait at the corner ")







def Backstories() :
    os.startfile('Backstories.py')

def hacktracker(i) :
    fout = open("TRACKHACK.txt", mode="r")
    s = fout.read()  # copy paste read part in main game
    i = s.count('\n')
#def Zammy()
#def CaptainGruMcFallow()
#def Sanjay()
#def Akshay()
#def Ayush()


w1 = w2 = w3 = w4 = w5 = 0
bonus_points =punish=0
print("Welcome to Kingdom of karma . . .")
playintro()
print("Menu :")
print("\t 1.New Game \n \t 2.Continue \n \t 3.Stats \n \t 4.Delete Save game")
i=int(input("Awaiting your command :"))
if i==1 :
    countdown(4)
    Gamer_name=input("\nPlease enter your name >>")
    time.sleep(1.2)
    print("\t\t\tNote : The choices you make will effect the outcome\n\n")
    time.sleep(1.99)
    print("Our story begins as the protagonist ", Gamer_name ," is seen aboard a SSWJ cargo plane")
    time.sleep(1.5)
    print(Gamer_name , "is an average 17 year old lad who has been recruited by the Indian army")
    print("Despite a young age ", Gamer_name ,"has P.T.S.D. ")
    print("His fellow comrades are preparing for an aerial attack on vietnam ",end=' ')
    print(". Yes, the world is at war . It is in fact world war 3")
    print("The Warm weather of Vietnam gently brisks our hero",Gamer_name,"'s scarred face")
    print("Our hero sits on the waiting seat waiting for his deployment signal.")
    print("CHOOSE YOUR ACTION :")
    print("\t 1. Talk to your comrades for debriefing \t 2.Visit the pilots in the cockpit \t")
    print("\t 3. Pass the time and skip your opportunity \t 4.Visit weapon's lot ")
    choice = {1: '1. Talk to your comrades' ,2 : '2. Visit the pilots',3 :'3. Pass the time',4:'4. Visit weapons lot' }
    i=int(input())
    print("You have chosen :",end=' ')
    time.sleep(0.8)
    print(choice[i])
    time.sleep(1)
    if i<0 or i>4 :
        print("Well you managed to mess it up huh?")
        time.sleep(1.5)
        print("Well your punishment is ACTION 3. Don't worry , this one won't effect your story's end .")
        time.sleep(1.5)
        print("\t\t\t Your welcome .")
        countdown(2)
    if i==1 :
        bonus_points+=1
        s1_1(Gamer_name)
        s1_2(Gamer_name)
    if i==2 :
        s1_2(Gamer_name)
    if i==3:
        punish-=1

