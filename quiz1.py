print("welcome")
n = input("what is your name? ")
playing =input("ok,"+str(n)+" Do You want to start the game? ")  
if playing.lower() != "yes":
    print("ok bye")
    quit()
print("ok ,Lets Play")
score=0
answer= input("1. What is the Capital of india? ")
if answer =="New Delhi":
    print("correct")
    score +=1
else: print(" Wrong answer is New Delhi")

answer= input("2. What is the Capital of TamilNadu? ")
if answer =="Chennai":
    print("correct")
    score +=1
else: print(" Wrong answer is Chennai")

answer= input("3. Where does Taj mahal located? ")
if answer =="Agra":
    print("correct")
    score +=1
else: print(" Wrong answer is Agra")

answer= input("4. what is ISRO located? ")
if answer =="Bangalore":
    print("correct")
    score +=1
else: print(" Wrong answer is Bangalore")

answer= input("5. when did india got independence? ")
if answer =="1947":
    print("correct")
    score +=1
else: print(" Wrong answer is 1947")

answer= input("6. what is CPU stands for? ")
if answer.lower() =="central processing unit":
    print("correct")
    score +=1
else: print(" Wrong answer is central processing unit ")

answer= input("7. national flower of india? ")
if answer.lower() =="lotus":
    print("correct")
    score +=1
else: print(" Wrong answer is lotus")

print("you got "+str( score)+" answers Correct")





