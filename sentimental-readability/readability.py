from cs50 import get_string
# TODO

# for user input
user_input = get_string("Text: ")

letters = 0
words = 1 
sentences = 0
# Loop over user_input and get the number of letters, words and sentences in the user_input
for i in user_input:
    if i.islower() or i.isupper():
        letters += 1
    if i == ' ':
        words += 1
    if i == '?' or i == '!' or i == '.':
        sentences += 1

# Letters and Sentences per 100 words
L = letters * 100 / words
S = sentences * 100 / words

# Coleman-Liau formula
grade = round(0.0588 * L - 0.296 * S - 15.8)

if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade}")
