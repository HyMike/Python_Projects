from random import choice


def select_word():
    with open("words.txt", mode='r') as words:
        reading_lines = words.readlines()
        return choice(reading_lines).strip()


selected_word = list(select_word().lower())
word_length = len(selected_word)

player1_guess = ["-"] * word_length

print(" ".join(player1_guess))
print(selected_word)


# Get the user player one input
counter = 6
while counter > 0:
    listening = input("Enter your input \n")
    one_exist = 0
    for index, char in enumerate(selected_word):
        if listening == char:
            player1_guess[index] = char
            print(" ".join(player1_guess))
            one_exist += 1
    if (one_exist < 1):
        counter -= 1
        print(f"That is incorrect. You have {counter} lives left. Please try again!\n")
        print(" ".join(player1_guess))

print("You lose!")


# create an array that will store all the correct values first starting out with ----- lines after replacing each with the correct value.
# Using the length of the selected String.


# create a counter for 6 tries if you get more you lose
# if you guess all the letters you win
# each turn will check this logic
