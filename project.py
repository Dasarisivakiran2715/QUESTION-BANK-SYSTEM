from random import sample
from users import usernames

class InvalidUserError(Exception):
    def __init__(self,m):
        self.msg=m
    def __str__(self):
        return "User user name or pwd are incorrect"+self.msg


def menu():
    print("1.Add Questions")
    print("2.Take Assesment")
    print("3.Get Score")
    print("4.Exit")

def addQs():
    print("\t1.Through Console")
    print("\t2.File Copy")
    c=int(input("Enter UR choice:"))
    if c==1:
        print("..........Through console....")
        fqb=open("QBank.txt","a")
        q=input("Enter the Q :")
        op1=input("OP1:")
        op2=input("OP2:")
        op3=input("OP3:")
        op4=input("OP4:")
        ans=input("ANS:")
        fqb.write(q+"#"+op1+"#"+op2+"#"+op3+"#"+op4+"#"+ans+"\n")
        fqb.close()
    elif c==2:
        print(".......File copying.......")
        fname=input("Enter the file name:")
        fp=open(fname,"r")
        fc=fp.read()
        fqb=open("QBank.txt","a")
        fqb.write(fc)
        fp.close()
        fqb.close()

uname=input("Enter user name :")
pwd=input("Enter Password :")
if usernames.get(uname)==pwd:
    print("Valid User....")
else:
    print("Invalid User...")
    try:
        raise InvalidUserError(uname)
    except InvalidUserError as ob:
        print(ob)
    exit()
while True:
    menu()
    ch=int(input("Enter UR choice:"))
    if ch==1:
        #print("Adding of Qs")
        addQs()
    elif ch==2:
        score=0
        print("Take Assesment...")
        n=int(input("How many Qs that U Would like to have in Assesment:"))
        fqb=open("QBank.txt","r")
        QL=fqb.readlines()
        #print(type(QL))
        fqb.close()
        #print(QL)
        RL=sample(QL,n)
        #print(RL)
        for Q in RL:
            Q=Q.strip()
            #print(Q)
            Q=Q.split("#")
            #print(Q)
            Qname=Q[0]
            op1=Q[1]
            op2=Q[2]
            op3=Q[3]
            op4=Q[4]
            ans=int(Q[5])
            print("Q :",Qname)
            print("1.",op1)
            print("2.",op2)
            print("3.",op3)
            print("4.",op4)
            a=int(input("Enter UR answer : "))
            if a==ans:
                score=score+1
            else:
                score=score-0.25
        print("UR score is :",score)
    elif ch==3:
        print("Your Score is :",score)
    elif ch==4:
        print("Thak U...")
        exit()
