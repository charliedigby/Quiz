# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 17:13:04 2025

@author: charl
"""

"""
Attempt to create quiz
"""
#Survey questions assign each answer to a variable, 
#with an index for each person
qu=[]
que=[]
fe=[]
field=input("What question do you want in the survey?\n")
t=0
ww=[]
while field!="continue":
    fe.append(field)
    ww.append([])
    print("\nHow will the quiz question be phrased for this field?\nType the text that precedes the survey response, press enter, then type the remaining text:")
    qu.append(input(""))
    que.append(input(""))
    print("\nThe survey questions currently are:")
    for i in range(t+1):
        print(fe[i])
    field=input("\nWhat question do you want in the survey?\n")
    while field=="delete" and t!=-1:
        print("The question,\"",fe[-1],"\", has been deleted")
        fe.pop(-1)
        ww.pop(-1)
        qu.pop(-1)
        que.pop(-1)
        t=t-1      
        field=input("\nWhat question do you want in the survey?\n")
    t=t+1


#%% survey
a=0
from random import randint as ra
name=[]


while a in range(12):
    nam=input("What is your name?\n").upper()
    while nam in name:
        print("Sorry, someone with your name has already filled in the survey, please try again with a variation, i.e. an initial, to distinguish you from",nam)
        nam=input("What is your name?\n").upper()
    name.append(nam)
    for u in range(t):
        print(fe[u])
        ww[u].append(input(""))
    a=a+1
    for p in range(50): print("\n")
    print("Thankyou!\nAnswers have been collected from")
    for x in range(a): print(name[x])
    c=input("")
    while c=="delete" and a!=0:
        print(name.pop(-1),"'s answers have been deleted")
        a=a-1
        for z in range(t):
            ww[z].pop(-1)
        c=input("")
    if c=="continue":break
    

#%% quiz
score=[0 for i in range(a)]



def take_guess(v,h):  
    if h==1:
        return True
    elif not v in name:
        print("Your guess was not a name in the survey, enter one of the following names:")
        for i in range(a): print(name[i])
        print("Try again,",name[x],":")
        return False
    elif v in gg:
        print("You have already guessed this answer for this question \nplease give a different answer,",name[x],":")
        return False
    elif v==name[x]:
        print("You are not allowed to guess yourself, try another guess,",name[x])
        return False
    
    else:
        return True

for u in range(t):
    xx=[i for i in range(a)]
    cx=[]
    c=a
    while c>0:
        b=ra(0,c-1)
        cx.append(xx[b])
        xx.pop(b)
        c=c-1
    y=0
    qq=[]
    while y in range(a): 
        qwerty=0
        q=0
        pp=[]
        for x in range(a):
            if ww[u][x]==ww[u][cx[y]]:
                q=q+1
                pp.append(name[x])
        print(qu[u],ww[u][cx[y]],que[u])
        if q>1: print("(",q,"answers )")
        for x in range(a):
            gg=[]
            if q==1:
                print(name[x],"'s guess:")
                guess=input("").upper()
                if guess=="SKIP" and x==0:
                    qwerty=1
                while take_guess(guess,qwerty)==False:
                    guess=input("").upper()
                if guess==name[cx[y]] and qwerty==0:
                    score[x]=score[x]+1             
            else:            
                for w in range(1,q+1):
                    print(name[x],"'s guess, (",w,"/",q,"):")
                    guess=input("").upper()
                    if guess=="SKIP" and x==0:
                        qwerty=1
                    while take_guess(guess,qwerty)==False:
                        guess=input("").upper()
                    gg.append(guess)
                    if guess in pp and qwerty==0:
                        score[x]=score[x]+1
            
        qq.append(ww[u][cx[y]])
        
        while ww[u][cx[y]] in qq and y!=a-1: 
            y=y+1
        if qwerty==1:
            y=a
       
    
    print("\nAnd the answers are...")
    for x in range(a):
        print(name[x],":\n           ",ww[u][x])
    if u!=t-1:
        print("\nThe score so far:")
        for x in range(a):
            print(name[x],":\n           ",score[x])
    else:
        print("\nThe final scores are:")
        for x in range(a):
            print(name[x],":\n           ",score[x])
        
    