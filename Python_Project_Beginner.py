print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, 15 "))
split = int(input("How many people to split the bill? "))

tippercent = tip / 100
totaltip = bill * tippercent
total_bill = bill + totaltip
bill_per_person = total_bill / split
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount} ")