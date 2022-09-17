from cs50 import get_string
# TODO

# for user input
user_input = get_string("Text: ")

l = 0
w = 1
s = 0
# loop for every character in the string given by the user
for character in user_input:
    if character.islower() or character.isupper():
        l += 1
    if character == ' ':
        w += 1
    if character == '?' or character == '!' or character == '.':
        s += 1

# Letters and Sentences per 100 words
L = l * 100 / w
S = s * 100 / w

# Coleman-Liau's formula
grade = round(0.0588 * L - 0.296 * S - 15.8)

if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade}")
