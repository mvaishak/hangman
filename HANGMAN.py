import random 

def game():
    secret = ['python', 'java', 'kotlin', 'javascript']
    ran = random.choice(secret)
    hidden = "-"*(len(ran))
    box = list(hidden)
    tried=[]
    n = 8
    while (n>0):
        print('\n')
        print(hidden)
        i = input("Input a letter:")
        if len(i) != 1:
            print("You should input a single letter")
        else:
            if i in tried:
                print("You already typed this letter")
            else:
                if i.islower() == False:
                    print("It is not an ASCII lowercase letter")
                else:
                    tried.append(i)
                    present = False
                    for t in range(len(ran)):
                        if ran[t] == i:
                            box[t] = i
                            present = True
                    hidden = "".join(box)
                    if present == False:
                        print("No such letter in the word")
                        n -= 1
                    present = False 
        if hidden == ran:
            print("You guessed the word {}!\nYou survived!".format(ran))            
    if hidden != ran:
        print("You are hanged!")

print("H A N G M A N")
option = ""
while option != 'exit':
    option = input('Type "play" to play the game, "exit" to quit:')
    if option == 'play':
        game()

                
    