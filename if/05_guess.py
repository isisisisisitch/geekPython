import random
#random.randint(min,max)
computer = random.randint(0,2)
print(computer)

player=int(input('lets go：0-rock，1-scissors，2-paper：'))
#player win
if((player==0)and (computer==1) or (player==1)and (computer==2) or (player==2)and (computer==0)):
    print("player win")
#tied game
elif player==computer:
    print("tied game ")
#computer win
else:
    print("computer win")