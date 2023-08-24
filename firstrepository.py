#twist is that you can't use the same thing two times in a row

print("Let's play rock paper scissors! Except with a twist: you can't use the same thing two times in a row.")

def start_round():
    your_move = int(input("Choose your move, type 1 for rock, 2 for paper, and 3 for scissors:"))

start_round()

robot_choices = [1, 2, 3]
robot_choice = random.choice(robot_choices)

def play_game():
    if robot_choice == your_move:
        print("tie! keep going")
        start_round()
    elif robot_choice == 1 and your_move == 3:
        print("you lose :(")
    elif robot_choice == 3 and your_move == 1:
        print("you win!")
    elif robot_choice == 1 and your_move == 2:
        print("you win!")
    elif robot_choice == 2 and your_move == 1:
        print("you lose :(")
    elif robot_choice == 2 and your_move == 3:
        print("you win!")
    elif robot_choice == 3 and your_move == 2:
        print("you lose :(")
    else:
        print("something went wrong")


play_game()
