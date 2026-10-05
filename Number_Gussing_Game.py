import random

MY_NUMBER = random.randint(1, 1000)
print("Guess My Number(1 - 1000):")
User_Number = int(input("Enter Your Guess: "))

while User_Number != 0:
    
    if MY_NUMBER == User_Number:
        print("Great, Number is Correct!")
        break
    
    elif MY_NUMBER > User_Number:
        print("Number is too Small...")

    else:
        print("Number is too Large...")

    User_Number = int(input("Try Again ( 0 to Stop):"))

print("My Number Was:",MY_NUMBER)