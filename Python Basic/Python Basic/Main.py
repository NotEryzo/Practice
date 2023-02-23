# # Triangle perimeter assignment

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

# Student Grades assignment

import random

array = []
for i in range(35):
    array.append(random.randint(0, 100))

while True:
    print("\nMain Menu")
    print("1. Display All Grades")
    print("2. Display Honours")
    print("3. Stats")
    print("4. Randomize Grades")
    print("5. Exit")
    choice = int(input("Select an option (1-5): "))

    if choice == 1:
        print("\nAll Grades\n")
        for i in array:
            print(str(i) + "%")
    elif choice == 2:
        numofH = 0
        print("\nHonours\n")
        for i in array:
            if i > 80:
                print(str(i) + "%")
                numofH += 1
        print("\nNumber of Honours: " + str(numofH))
    elif choice == 3:
        pass
