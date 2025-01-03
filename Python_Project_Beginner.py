print("Welcome")
height = int(input("What is your height? "))
bill = 0

if height >= 4:
    print("You can ride!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child ticket is $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7")
    else:
        bill =12
        print("Adult ticket is $12")

    want_photo = input("Do you want a photo Y or N? ")
    if want_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")
    
else:
    print("Sorry you cannot ride")
