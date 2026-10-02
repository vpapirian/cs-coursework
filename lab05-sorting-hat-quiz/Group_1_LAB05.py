print("Answer the following questions with a number between 1 and 4")

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

answer_1 = int(input(""" Q1) Do you enjoy nighttime or daytime more?

1) Daytime
2) Nighttime

"""))

if answer_1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer_1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Report to Dumbledore's chambers immediately!")


answer_2 = int(input(""" Q2) If you saw a classmate cheating on an exam, what would you do?

1) Tell on them.
2) Let it go.
3) Try to convince them after the exam to not cheat anymore.
4) Try to cheat off of them.



"""))

if answer_2 == 1:
    ravenclaw += 1
elif answer_2 == 2:
    hufflepuff += 1
elif answer_2 == 3:
    gryffindor += 1
elif answer_2 == 4:
    slytherin += 1
else:
    print("Report to Dumbledore's chambers immediately!")


answer_3 = int(input(""" Q3) What do you want to be remembered as?

1) The Good
2) The Great
3) The Wise
4) The Bold


"""))

if answer_3 == 1:
    hufflepuff += 2
elif answer_3 == 2:
    slytherin += 2
elif answer_3 == 3:
    ravenclaw += 2
elif answer_3 == 4:
    gryffindor += 2
else:
    print("Report to Dumbledore's chambers immediately!")



max_score = max(ravenclaw, hufflepuff, slytherin, gryffindor)
if ravenclaw == max_score:
    print("Ravenclaw!!!")
elif hufflepuff == max_score:
    print("Hufflepuff!!!")
elif slytherin == max_score:
    print("Slytherin!!!")
elif gryffindor == max_score:
    print("Gryffindor!!!")

