from cs50 import get_string
# TODO

# for user input
user_input = get_string("Text: ")

l = 0
w = 1
s = 0
# Loop over user_input and get the number of l, w and s in the user_input
for character in user_input:
    if character.islower() or character.isupper():
        l += 1
    if character == ' ':
        w += 1
    if character == '?' or character == '!' or character == '.':
        s += 1

# Letters and Sentences per 100 w
L = l * 100 / w
S = s * 100 / w

# Coleman-Liau formula
grade = round(0.0588 * L - 0.296 * S - 15.8)

if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade}")
