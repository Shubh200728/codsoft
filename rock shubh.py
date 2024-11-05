import random
r=0
c=0
u=0
print("\n Game: rock*paper*scissors!")
def replay(r,u,c):
    print("Enter 'rock','paper', or 'scissors' to play.")
    user=input("enter your choice (rock:paper:scissor)-").lower()
    if user not in ["rock","paper","scissors"]:
        print("invailed choice. pleases eneter rock, paper, scissor")
        replay(r,u,c)
    computer=random.choice(['rock','paper','scissor'])
    r+=1
    if user == 'rock':
        a=winner(user,computer)
        if a=="c":
            c+=1
        elif a=="u":
            u+=1
        again=input("Enter 'yes' for to play next round and 'no' for to exit-").lower()
        if again=='yes':
            print("\nscore after",r,"rounds")
            print("user:",u," | computer:",c)
            replay(r,c,u)
        elif again == 'no':
            print("\nthankyou for playing! final score after-",r)
            print("user:",u," | computer:",c)
            print("\nthankyou for playing.")
        else:
            eror(r)
    elif user == 'paper':
        a=winner(user,computer)
        if a=="c":
            c+=1
        elif a=="u":
            u+=1
        again=input("Enter 'yes' for to play next round and 'no' for to exit-").lower()
        if again=='yes':
            print("\nscore after",r,"rounds")
            print("user:",u," | computer:",c)
            replay(r,c,u)
        elif again == 'no':
            print("\nthankyou for playing! final score after-",r)
            print("user:",u," | computer:",c)
            print("\nthankyou for playing.")
        else:
            eror(r)
    elif user == 'scissors':
        a=winner(user,computer)
        if a=="c":
            c+=1
        elif a=="u":
            u+=1
        again=input("Enter 'yes' for to play next round and 'no' for to exit-").lower()
        if again=='yes':
            print("\nscore after",r,"rounds")
            print("user:",u," | computer:",c)
            replay(r,c,u)
        elif again == 'no':
            print("\nthankyou for playing! final score after-",r)
            print("user:",u," | computer:",c)
            print("\nthankyou for playing.")
        else:
            eror(r)
def winner(user,computer):
    if user == computer:
        print("tie")
    elif (user == "rock" and computer == "scissor") or \
         (user == "scissor" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("user win")
        return "u"
    else:
        print("computer win")
        return "c"
def eror(r):
        print("invailed input!")
        again=input("Enter 'yes' for to play next round and 'no' for to exit-").lower()
        if again == 'yes':
            r-=1
            replay(r,c,u)
        elif again == "no":
            print("\nthankyou for playing! final score after-",r)
            print("user:",u," | computer:",c)
            print("\nthankyou for playing.")
        else:
            eror(r)
replay(r,u,c)


    