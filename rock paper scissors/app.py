from random import choice

options = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}

possible_options = ["R", "P", "S"]

while True:
    print("Pick an option")
    print("R - Rock")
    print("P - Paper")
    print("S - Scissors")
    user_option = input(">>> ")
    user_option = user_option.upper()

    if user_option not in possible_options:
        print("\nInvalid option. You can only enter \"R\", \"P\" or \"S\"\n")
        continue

    computer_option = choice(possible_options)

    print(f"\nPlayer ({options[user_option]}): CPU ({options[computer_option]})\n")

    if user_option == computer_option:
        print("It's a tie\n")
    else:
        if user_option == "R" and computer_option == "S":
            print("You win")
            break
        elif user_option == "S" and computer_option == "R":
            print("CPU wins")
            break
        elif user_option == "S" and computer_option == "P":
            print("You win")
            break
        elif user_option == "P" and computer_option == "S":
            print("CPU wins")
            break
        elif user_option == "P" and computer_option == "R":
            print("You win")
            break
        elif user_option == "R" and computer_option == "P":
            print("CPU wins")
            break