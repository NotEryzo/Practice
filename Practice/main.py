# Caught Speeding

# print("Welcome to the caught speeding program!")
# print("Enter the speeds and speed limits for 3 drivers to determine the type fo ticket they will recieve... ")

# print("\n Driver 1")
# d1 = int(input("Enter speed for driver 1: "))
# speedd1 = int(input("Enter speed limit for driver 1: "))

# print("\n Driver 2")
# d2 = int(input("Enter speed for driver 2: "))
# speedd2 = int(input("Enter speed limit for driver 2: "))

# print("\n Driver 3")
# d3 = int(input("Enter speed for driver 3: "))
# speedd3 = int(input("Enter speed limit for driver 3: "))


# def determineTicket(speed, limit):

#     if speed > limit + 40:
#         return "Really Big Ticket"
#     elif speed > limit + 20:
#         return "Big Ticket"
#     elif speed > limit:
#         return "Small Ticket"
#     else:
#         return "No Ticket"


# print('\n Ticket Results: ')
# print('Driver 1 Ticket Type: ' + str(determineTicket(d1, speedd1)))
# print('Driver 2 Ticket Type: ' + str(determineTicket(d2, speedd2)))
# print('Driver 3 Ticket Type: ' + str(determineTicket(d3, speedd3)))

# ----------------------------------------------------------------------------------------------------

# Triangle perimeter assignment

# import math

# print("Welcome to the Triangle perimeter program")
# print('Enter the Coordinates of the vertices of a triangle...')

# print("\nVertex A")
# Ax = int(input("Enter x-coordinate for Vertex A: "))
# Ay = int(input("Enter y-coordinate for Vertex A: "))

# print("\nVertex B")
# Bx = int(input("Enter x-coordinate for Vertex B: "))
# By = int(input("Enter y-coordinate for Vertex B: "))

# print("\nVertex C")
# Cx = int(input("Enter x-coordinate for Vertex C: "))
# Cy = int(input("Enter y-coordinate for Vertex C: "))


# def dist(x1, y1, x2, y2):

#     distance = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
#     return distance


# ABdist = dist(Ax, Ay, Bx, By)
# ACdist = dist(Ax, Ay, Cx, Cy)
# BCdist = dist(Bx, By, Cx, Cy)

# perim = (ABdist + ACdist + BCdist)

# print("Side length and perimeter:")
# print("AB = " + str(ABdist))
# print("AC = " + str(ACdist))
# print("BC = " + str(BCdist))
# print("Perimeter of Triangle = " + str(perim))

# ----------------------------------------------------------------------------------------------------

# Dice Roll Simulator

# import random

# def roll2Dice():
#     num1 = random.randint(1, 6)
#     num2 = random.randint(1, 6)
#     sum = num1 + num2
#     print("\nThe sum of: " + str(num1) + " and " +
#           (str(num2) + " is " + str(sum)))
#     return sum


# while True:

#     print("\n Dice Roll Simulator Menu")
#     print("1. Roll Dice Once")
#     print("2. Roll Dice 5 times")
#     print("3. Roll Dice 'n' Times")
#     print("4. Roll Dice until Snake Eyes")
#     print("5. Exit")
#     choice = int(input("Select and option (1-5): "))

#     if choice == 1:
#         roll2Dice()
#     elif choice == 2:
#         for i in range(5):
#             roll2Dice()
#     elif choice == 3:
#         inputnum = int(input("How many times do you want to roll the Dice?: "))
#         for i in range(inputnum):
#             roll2Dice()
#     elif choice == 4:
#         count = 0
#         while True:
#             count += 1
#             sum = roll2Dice()
#             if sum == 2:
#                 print(f"\nIt took {count} many rolls to get Snake Eyes")
#                 break
#     elif choice == 5:
#         break
#     else:
#         print("\nThat is an invalid input")

# ---------------------------------------------------------------------------------------------

# Student Grades assignment

# import random

# array = []
# for i in range(35):
#     array.append(random.randint(0, 100))

# while True:
#     print("\nMain Menu")
#     print("1. Display All Grades")
#     print("2. Display Honours")
#     print("3. Stats")
#     print("4. Randomize Grades")
#     print("5. Exit")
#     choice = int(input("Select an option (1-5): "))

#     if choice == 1:
#         print("\nAll Grades\n")
#         for i in array:
#             print(str(i) + "%")
#     elif choice == 2:
#         numofH = 0
#         print("\nHonours\n")
#         for i in array:
#             if i > 80:
#                 print(str(i) + "%")
#                 numofH += 1
#         print("\nNumber of Honours: " + str(numofH))
#     elif choice == 3:
#         max_grade = max(array)
#         min_grade = min(array)
#         ave_grade = sum(array) / len(array)
#         print("\nStats\n")
#         print("Higherst Grade: " + str(max_grade) + "%")
#         print("Lowest Grade: " + str(min_grade) + "%")
#         print("Average Grade: " + str(round(ave_grade)) + "%")
#     elif choice == 4:
#         array.clear()
#         print("\n Grades have been Randomized\n")
#         for i in range(35):
#             array.append(random.randint(0, 100))
#         for n in array:
#             print(str(n) + "%")
#     elif choice == 5:
#         breaka
#     else:
#         print("That is an invalid input")

# --------------------------------------------------------------------

# Nickname generator 

fname = input("What is your first name?: ")
lname = input("What is your last name?: ")
fullname = fname + "" + lname

while True:
    print("\n Main Menu " + "(" + fullname + ")")
    print("1. Change Name")
    print("2. Display a Random Nickname")
    print("3. Display All Nicknames")
    print("4. Add a Nickname")
    print("5. Remove a Nickname")
    print("6. Exit")
    choice = int(input("Select an option (1-6): "))

    if choice == 1:
        print("Change Name")
        input



