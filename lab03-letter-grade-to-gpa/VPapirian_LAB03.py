#Write a Python script that:

letter_grade = input("Please enter a letter grade: ")
letter_grade = letter_grade.upper()
letter_grade = letter_grade.strip()
'''
prompts the user for a letter grade such as A, B-, C+, F
Use if...elif...else statements to convert the letter grade to a number GPA grade according to the the following rules:
(1) whole letters will convert to the numbers like so:

A = 4.0, B = 3.0, C = 2.0, D = 1.0, F = 0

(2) a '+' will add 0.3 to the GPA grade e.g. B+ = 3.3

        a  '-' will subtract 0.3 from the GPA grade e.g. B- = 2.7

(3) you can not have a GPA above 4.0 (A and A+ are both 4.0)

(4) F, F+ and F- are all equal to 0

prints the number grade to the user'''

if letter_grade == "A" or letter_grade == "A+":
    print(4.0)
elif letter_grade == "A-":
    print(3.7)
elif letter_grade == "B":
    print(3.0)
elif letter_grade == "B+":
    print(3.3)
elif letter_grade == "B-":
    print(2.7)
elif letter_grade == "C":
    print(2.0)
elif letter_grade == "C+":
    print(2.3)
elif letter_grade == "C-":
    print(1.7)
elif letter_grade == "D":
    print(1.0)
elif letter_grade == "D+":
    print(1.3)
elif letter_grade == "D-:":
    print(0.7)
elif letter_grade == "F" or letter_grade == "F+" or letter_grade == "F-":
    print(0.0)

