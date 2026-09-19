import random

def roll():
    return random.randint(1, 10)


while True:
    print("Give space to start: ")
    m = input()

    if m == " ":
        value = roll()

        match value:
            case 1:
                print("You got 1st program\nSimple Calculator")

            case 2:
                print("You got 2nd program\nDay of the Week")

            case 3:
                print("You got 3rd program\nMonth Name")

            case 4:
                print("You got 4th program\nGrade Calculator")

            case 5:
                print("You got 5th program\nMenu-Driven Program")

            case 6:
                print("You got 6th program\nArithmetic Operations")

            case 7:
                print("You got 7th program\nNumber to Word")

            case 8:
                print("You got 8th program\nTraffic Light")

            case 9:
                print("You got 9th program\nArea Calculator")

            case 10:
                print("You got 10th program\nUnit Converter")

    n = input("You want to stop? (n): ")

    if n.lower() == "n":
        print("Thank you")
        break