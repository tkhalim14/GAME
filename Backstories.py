import time
import os                  ##Backstories are like journals or diaries of teammates
# i need to make a suspicion tracker indicating how many times the account was hacked
def hacktracker(i):
    fout=open("TRACKHACK.txt",mode="r")
    fin=open("TRACKHACK.txt",mode='w')
    k = time.ctime()
    fin.write(k)
    fin.write('\n')
    s = fout.read()               # copy paste read part in main game
    i = s.count('\n')




def hackdown(t) :
    i=0
    print("Loading ,Hacking is in progress ",end=' ')
    while i<=t :
        print(t-i,"...",end='')
        time.sleep(1)
        i+=1

def countdown(t) :
    i=0
    print("Loading ,Hacking is in progress ",end=' ')
    while i<=t :
        print(t-i,"...",end='')
        time.sleep(1)
        i+=1

def filestarter(data) :
    if data==12134 :
        os.startfile('Zammy.txt')
    if data==43567 :
        os.startfile('Captain Gru Mcfallow.txt')
    if data==55678 :
        os.startfile('Sanjay.txt')
    if data==77755 :
        os.startfile('Akshay.txt')
    if data==99653 :
        os.startfile('Ayush.txt')
    else:
        if data!=12134 and data!= 43567 and data!=55678 and data!=77755 and data!=99653 :
          print('\n','{Hacking Unsuccessful}')
          time.sleep(3)
          print("Military ID doesn't exist in database")


#if c_code.lower=='help' :
#if c_code=='clear_LOGS':
#if c_code=='display_LOGS' :
#if c_code=='Hack_M.Database' :

print("Accessing Database.....")
time.sleep(2)
CODE=float(input("ENTER ENROLL CODE {The 5 digit code on the Military ID of the target} <<"))
data=[12134,43567,55678,77755,99653]
name=['Zammy','Captain Gru Mcfallow','Sanjay','Akshay','Ayush']
##the gamer must remember the military codes acquired from his teammates(illegally)
i=0
hackdown(3)
u = time.ctime()
while i>=0 and i<=4 :
     if CODE==data[i] :
         hacktracker()
         print('\n', '{Hacking successful}')
         time.sleep(3)
         print("Welcome Lietenant , ",name[i])
         print('Would you like to continue entry update?[y/n]')
         k=input()
         if k=='y':                         #need to create fn that puts time stamp
             if data[i]==12134 :
                 fout=open('Zammy.txt','a')
                 fout.write("\nNEW ENTRY AT :")
                 fout.write(u)
                 fout.write('\n')
             if data[i] == 43567:
                 fout = open('Captain Gru Mcfallow.txt', 'a')
                 fout.write("\nNEW ENTRY AT :")
                 fout.write(u)
                 fout.write('\n')
             if data[i] == 55678:
                 fout = open('Sanjay.txt', 'a')
                 fout.write("\nNEW ENTRY AT :")
                 fout.write(u)
                 fout.write('\n')
             if data[i] == 77755:
                 fout = open('Akshay.txt', 'a')
                 fout.write("\nNEW ENTRY AT :")
                 fout.write(u)
                 fout.write('\n')
             if data[i] == 99653:
                 fout = open('Ayush.txt', 'a')
                 fout.write("\nNEW ENTRY AT :")
                 fout.write(u)
                 fout.write('\n')
             countdown(5)
         if k=='n':
             print("Exiting Database .....")
     i+=1

filestarter(CODE)