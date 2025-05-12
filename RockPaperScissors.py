import random

while True:
    choices = ('r', 'p', 's')
    user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()

    if user_choice not in choices:
        print("Invalid choice!")
        continue

    computer_choice = random.choice(choices)

    print(f'You chose: {user_choice}')
    print(f'Computer chose: {computer_choice}')

    if user_choice == computer_choice:
        print("Tie!")
    elif (
            (user_choice == 'r' and computer_choice == 's') or
            (user_choice == 's' and computer_choice == 'p') or
            (user_choice == 'p' and computer_choice == 'r')
    ):
        print("You win!")
    else:
        print("You lose!")
