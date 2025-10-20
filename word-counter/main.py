print("Word Counter")

entered_expression = input("Please write the phrase you want to count words for: ")

expression_words = entered_expression.split()
print("Total word count: ", len(expression_words))

expression_letters = entered_expression.replace(" ", "").replace(".", "").replace(",", "")
print("Total letter count: ", len(expression_letters))