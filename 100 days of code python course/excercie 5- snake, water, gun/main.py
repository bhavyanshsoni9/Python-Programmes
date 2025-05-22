from random import choice  

choices = [0, 1, 2]
your_score = 0
comp_score = 0

i = 0

def win_lose():
    global user_input, computer_input, your_score, comp_score
    '''
    This function tells if user has won or lost and tells the score and write it in a file named score.txt
    '''
    # Tie 
    if user_input == computer_input :
        print("Tie!")

    # Win
    elif user_input == 0 and computer_input == 1:
        print("You Won!") 
        your_score = your_score + 1

    elif user_input == 1 and computer_input == 2:
        print("You Won!")
        your_score = your_score + 1

    elif user_input == 2 and computer_input == 0:
        print("You Won!")
        your_score = your_score + 1

    # Lose
    elif user_input == 1 and computer_input == 0:
        print("You Lose!")
        comp_score = comp_score + 1

    elif user_input == 2 and computer_input == 1:
        print("You Lose!")
        comp_score = comp_score + 1

    elif user_input == 0 and computer_input == 2:
        print("You Lose!")
        comp_score = comp_score + 1


def score():
    global your_score, comp_score
    
    with open("score.txt", 'w') as f:
        f.write(f"Your Score: {your_score}\n") 
        f.write(f"Computer Score: {comp_score}") 

while i < 10:
    i = i + 1
    try:
        computer_input= choice(choices)
        print(computer_input)
        user_input = int(input("Enter 0 for Snake, 1 for Water and 2 for Gun: "))
        win_lose()
        score()
    except ValueError as v:
        print("Invalid Input.Enter value from 0 to 2!")
        

print("Game Over!")