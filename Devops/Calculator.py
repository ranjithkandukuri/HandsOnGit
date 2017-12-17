def add(num1,num2):
    """Returns num1 plus num2"""
    return num1 + num2

def sub(num1,num2):
    """Returns num1 minus num2"""
    return num1 - num2

def mul(num1,num2):
    """Returns num1 times num2"""
    return num1 * num2

def div(num1,num2):
    """Returns num1 divided by num2"""
    return num1 / num2

def main():
    valid_input = False
    while not valid_input:
        """Allows user to run basic calculator with two numbers"""
        try:
            num1 = int(input("What is number 1? "))
            num2 = int(input("What is number 2? "))
            operation = int(input("Give the number of the operation you want to do. \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division\n"))
            valid_input = True
        except:
            try_again = input("Invalid input. Do you want to try again (y/n)?")
            if (try_again == 'n'):
                print("Exiting the program.\nHasta la vista!!")
                return
            else:
                print("\n")
        finally:
            print("\nThis will get executed no matter what")


    if (operation == 1):
        print(add(num1,num2))

    elif (operation == 2):
        print(sub(num1,num2))

    elif (operation == 3):
        print(mul(num1,num2))

    elif (operation == 4):
        print(div(num1,num2))

    else:
        print("Invalid operation")

main()
