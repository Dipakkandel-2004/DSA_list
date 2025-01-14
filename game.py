import random
compScore=0
userscore=0
def playgame():
    global compScore
    global userscore
    uservalue=input("Enter rock, paper or scissor ")
    val=["rock","paper","scissor"]
    random_value=random.randint(0,2)
    computervalue=(val[random_value])
    if(uservalue=="rock" and computervalue=="scissor"):
        print("user won")
        userscore+=1
    elif(uservalue=="paper" and computervalue=="scissor"):
        compScore+=1
        print("User lose")
    elif(uservalue=="scissor" and computervalue=="rock"):
        compScore+=1
        print("User lose")
    elif(uservalue=="scissor" and computervalue=="paper"):
        userscore+=1  
        print("user won")  
    elif(uservalue=="rock" and computervalue=="paper"):
        compScore+=1
        print("User lose")  
    elif(uservalue=="paper" and computervalue=="rock"):
        userscore+=1    
        print("user won")
    else:
        print("Draw")    
    print("User-score is ",userscore)    
    print("Computer-score is ",compScore,"\n") 
i=0       
while(i<=3):
    playgame()
    i+=1

        

