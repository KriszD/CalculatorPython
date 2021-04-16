import math
import sys

# This prints basic information about what this code is
print("\033[1m", "This is a calculator in python.  Made by Krisztian Drimba.", "\033[0m")

# Begins the while loop, and runs it as long as i is greater than 1 (it always is)
i = 1
while i >= 1:

    # Prints the options in the menu and tells the user to input a choice
    print("\nCalculator")
    print("Info")
    print("Exit")
    menu = input("\nPlease input ONE of the choices (Type in one of the words above with NO capitals): ")

    # If the player chose calculator from the menu, it then prints the options for what operations/calculations he can choose from
    if menu == "calculator":
        print("----------------------------------------------------------------------------")
        print("\033[1m", "Math Operations:", "\033[0m")
        print("Addition, Subtraction, Multiplication, Division, Power, Root")
        print("\033[1m", "\nGeometrical Operations:", "\033[0m")
        print("Pythagorean Calculator, Area of Shapes")
        choice = input("\nPlease input ONE of the choices (FIRST WORD of the operation, NO capitals): ")

        # If the player then chooses to do the addition calculation, it will ask for two numbers and then use the selected operation and output it
        if choice == "addition":
            add_1 = input("Input the first number")
            add_2 = input("Input the second number")
            sum = float(add_1) + float(add_2)
            print(add_1, "+", add_2, "=", sum)

        # If the player then chooses to do the subtraction calculation, it will ask for two numbers and then use the selected operation and output it
        elif choice == "subtraction":
            sub_1 = input("Input the first number")
            sub_2 = input("Input the second number")
            difference = float(sub_1) - float(sub_2)
            print(sub_1, "-", sub_2, "=", difference)

        # If the player then chooses to do the multiplication calculation, it will ask for two numbers and then use the selected operation and output it
        elif choice == "multiplication":
            mul_1 = input("Input the first number")
            mul_2 = input("Input the second number")
            product = float(mul_1) * float(mul_2)
            print(mul_1, "*", mul_2, "=", product)

        # If the player then chooses to do the division calculation, it will ask for two numbers and then use the selected operation and output it
        elif choice == "division":
            div_1 = input("Input the first number")
            div_2 = input("Input the second number")
            quotient = float(div_1) * float(div_2)
            print(div_1, "/", div_2, "=", quotient)

        # If the player then chooses to do the power calculation it will get the number and the value of its power
        elif choice == "power":
            pow_1 = input("Input the number")
            pow_2 = input("Input the number's power")
            pow = float(pow_1) ** float(pow_2)
            print(pow_1, "to the power of", pow_2, "=", pow)

        # If the player then chooses to do the root calculation it will get the number and the value of its root
        elif choice == "root":
            root_1 = input("Input the number")
            root_2 = input("Input how much its being rooted by")
            root = round(math.pow(float(root_1), 1/float(root_2)))
            print("The", root_2, "root of", root_1, "=", root)

        # If the player chooses the pythagorean theorem, it will get the values of a and b to find c
        elif choice == "pythagorean":
            pythagorean_1 = input("Input the first number")
            pythagorean_2 = input("Input the second number")
            pythagorean = math.sqrt((float(pythagorean_1) ** 2 + float(pythagorean_2) ** 2))
            print("The hypotenuse of ", pythagorean_1, "and", pythagorean_2, "is", round(pythagorean, 2))

        # If the player chooses area, it will then go to the if statement inside of the area if statement, and ask the user what shape they want to find the area for
        elif choice == "area":
            print("Square")
            print("Rectangle")
            print("Triangle")
            print("Circle")
            choice2 = input("Please choose a shape to calculate the area of:")

            # If the player chooses square, it asks for the side length and calculates the area
            if choice2 == "square":
                length = input("Input a side length")
                area = float(length) ** 2
                print("The area of a square is", area)

            # If the player chooses rectangle, it asks for the side length and width and calculates the area
            elif choice2 == "rectangle":
                length = input("Input the length")
                width = input("Input the width")
                area = float(length) * float(width)
                print("The area of a rectangle is", area)

            # If the player chooses triangle, it asks for the base and height and calculates the area
            elif choice2 == "triangle":
                base = input("Input the base")
                height = input("Input the height")
                area = (float(base) * float(height))/2
                print("The area of a triangle is", area)

            # If the player chooses circle, it asks for the radius and calculates the area
            elif choice2 == "circle":
                radius = input("Input the radius")
                area = 3.14*(float(radius) ** 2)
                print("The area of a circle is", area)

        # If the player chooses the pythagorean theorem, it will get the values of a and b to find c
        elif choice == "average":
            avg_1 = input("Input the first number")
            avg_2 = input("Input the second number")
            avg = (float(avg_1) + float(avg_2)) / 2
            print("The average of", avg_1, "and", avg_2, "is", avg)

        # If they input something that is not a choice then it says the input is invalid
        else:
            print("Invalid Input")

    # If the player chooses info in the menu it displays info about the calculator
    elif menu == "info":
        print("\nThis is a calculator made by Krisztian Drimba in python. I coded this in my spare time and at school.")
        print("Very soon it will be able to calculate many many things.")
        print("Including mathematical formulas, all the way to geometrical equations.")
        print("As I make this I hope anyone who uses it enjoys it.")
        print("The original was made in C But now I made it in python. :)")

    # If the player chooses exist in the menu it ends the code
    elif menu == "exit":
        sys.exit()

# This adds 1 to the count of the while loop
i += 1
