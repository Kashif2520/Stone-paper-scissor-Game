import random

def game():
    matrix = [
        ["Draw","you Lose","You won"],
        ["You Won","Draw","you lose"],
        ["you lose","You won","Draw"]
    ]

    values = ["rock","paper","scissor"]

    while True:
        comp = random.choice([0,1,2])
        print("\n0.Rock\n1.paper\n2.scissor\n3.exit\n")
        user = int(input("enter number:- "))
        if user == 3:
            break    
        if user not in (0,1,2,3):
            print("Select only from 0,1,2 and 3")
            game()

        result = matrix[user][comp]
        print(f"\ncomp select {values[comp]} and you select {values[user]}\nresult:- {result}")

game()