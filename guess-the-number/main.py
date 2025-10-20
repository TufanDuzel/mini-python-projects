import random

print("Guess The Number")

number = random.randint(0, 100)

selected_number = 0

while selected_number != number:
    selected_number = int(input("Enter a number: "))

    if selected_number > number:
        print("Try a smaller number!")
    elif selected_number < number:
        print("Try a larger number! ")

print("Congratulations, you find the number!")