import time

stack = []
b = 1
print("Welcome to Mynote")
time.sleep(1)
print("A virtual memo file database system created by Tabish Khalid Halim")
time.sleep(3)
while b > 0:
    print("So User what would you like to do?")
    print("1. Create new memo")
    print("2. Open existing memos")
    print("3. Delete memo [ONLY THE WORDs]")
    print("4. Edit existing memo [ONLY WORDS]")
    print("5. Add a new memo to your list")
    print("6. Exit program")
    q = int(input("Enter the no. code {1,2,3,4,5,6}\n"))
    if q == 1:
        print("Creating new memo :")
        i = 1
        while i > 0:
            d = input(".")
            stack.append(d)
            print("DO YOU WISH TO CONTINUE ?[5 for exit,0 for continue]")
            s = int(input())
            if s == 5:
                break
            i += 1
        j = 0
        f = open("Data.txt", "w")
        while j < i:
            o = stack[j]
            f.write(o)
            f.write("\n")
            j += 1
        f.close()
        time.sleep(5)
    if q == 2:
        print("Opening list of your memos :")
        f1 = open("Data.txt", "r")
        if f1.mode == "r":
            stack = f1.read()
            print(stack)
        f1.close()
        time.sleep(5)
    if q == 3:
        print("Which memo would you like to delete ?")
        print("Opening list of your memos :")
        f1 = open("Data.txt", "r")
        if f1.mode == "r":
            stack = f1.read()
            print(stack)
        f1.close()
        k = input()  # k is the one to get replaced by other text
        fin = open("Data.txt", "rt")
        data = fin.read()
        data = data.replace(k, "")
        fin.close()
        fou = open("Data.txt", "wt")
        fou.write(data)
        fou.close()
        time.sleep(5)
    if q == 4:
        print("Which one would you like to edit ?")
        print("Opening list of your memos :")
        f1 = open("Data.txt", "r")
        if f1.mode == "r":
            stack = f1.read()
            print(stack)
        f1.close()
        k = input()  # k has the same str function as above
        i = input("Enter value to be replaced by")
        fin = open("Data.txt", "rt")
        data = fin.read()
        data = data.replace(k, i)
        fin.close()
        fou = open("Data.txt", "wt")
        fou.write(data)
        fou.close()
        time.sleep(5)
    if q == 5:
        print("Creating new memo :")
        i = 1
        while i > 0:
            d = input(".")
            stack.append(d)
            print("DO YOU WISH TO CONTINUE ?[5 for exit,0 for continue]")
            s = int(input())
            if s == 5:
                break
            i += 1
        j = 0
        f = open("Data.txt", "a")
        while j < i:
            o = stack[j]
            f.write(o)
            f.write("\n")
            j += 1
        f.close()
        time.sleep(5)
    if q == 6:
        break
