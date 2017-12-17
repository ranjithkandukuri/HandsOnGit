def helloRanjith(mystring):
    print(mystring)
    first_name = input("First Name? ")
    sib_num = input("How many siblings do you have? ")
    if(first_name == "Ranjith" and sib_num == 1):
        print("You are Ranjith Kandukuri")
    elif(first_name == "Ranjith" and sib_num != 1):
        print("You are Ranjith but not Kandukuri")
    else:
        print("You are not Kanudukuri")
helloRanjith("Namaste")
helloRanjith("Vanakkam")
