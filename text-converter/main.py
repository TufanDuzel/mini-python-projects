print("Text Converter")

text = ""
word_counter = ""
action = ""

while True:
    text = str(input("Please enter the text: "))
    action = str(input("Please select the action you want to do: \n(Upper), (Lower), (Title). \n"))
    letter_counter = input("Please enter the letter you want to count: ")
    if action == "Upper":
        print(action.upper())
        print("Count: ", text.count(letter_counter))
        break
    elif action == "Lower":
        print(text.lower())
        print("Count: ", text.count(letter_counter))
        break
    elif action == "Title":
        print(text.title())
        print("Count: ", text.count(letter_counter))
        break
    else:
        print("You entered the wrong action.")