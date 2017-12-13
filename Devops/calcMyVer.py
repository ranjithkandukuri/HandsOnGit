num1 = int(input("Give a number: "))
num2 = int(input("Give another number: "))
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
def main():
    operation = input("What do you want? (+,-,*,/)")
    if(operation == "+"):
        print(add)
    elif(operation == "-"):
        print(sub)
    elif(operation == "*"):
        print(mul)
    elif(operation == "/"):
        print(div)
    else:
        print("invalid operator")
main()
