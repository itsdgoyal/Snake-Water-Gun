#------------------------------SNAKE WATER GUN---------------------------------#
print("****************** SNAKE WATER AND GUN ****************** \n")
print("This Game is created by Deepansh Goyal \n")
print("-------- E N J O Y -------- \n")
print("Rules:-")
print(" -> Never Give Up XD \n -> There are total 10 rounds \n -> This game contain random opponent")

import random
c=0
u1=0
for i in range(0,10):
   
    print("Enter that u want s/w/g")
    u=input()
    lst = ['s','w','g']
    comp=random.choice(lst)
    print(comp)
    
    if ((u=='s'  and comp=='g')or(u=='g' and comp=='w')or(u=='w' and comp=='s')):
        print ("computer won the game")
        c=c+1
    elif((u=='g' and  comp=='s')or(u=='s' and comp=='w')or(u=='w' and comp=='g')):
        print ("user won the game")
        u1+=1
    else:
        print("game tie")

print("computer win:", c)
print("user win:",u1)