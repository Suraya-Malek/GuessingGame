import random
game_done="n"
play=input("Do you want to play a guessing game? (y/n)")

while game_done =="n":
    if (play == "y"):
        print("Guess the number!")
        limit = int(input("Enter a limit:"))
        print("I'm thinking of a number from 1 to", limit)
        right_num = random.randint(1, limit)
        guess = int(input("what is your guess:"))
        tries = 1
        while guess != right_num:
            if right_num>guess:
                print("Too low")
            if right_num<guess:
                print("Too high")
            guess = int(input("What is your new guess:"))
            tries = tries + 1
        print("Good job, the game is done")
        print("You got the number in", tries, "tries")
    game_done = input("Are you done playing this game (y/n)")
print("thanks for playing")  
            
            

        