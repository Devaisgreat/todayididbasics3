# my own solution

print("Welcome to the tip calculator.")
total_bill = input("What is your total bill? ")
tip_percentage = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")
split_the_bill = input("How many people to split the bill? ")

float_total_bill = float(total_bill)
int_tip_percentage = int(tip_percentage)
int_split_the_bill = int(split_the_bill)
eventual_total_bill = float_total_bill * 0.01 * (100 + int_tip_percentage)
final_payment = eventual_total_bill / int_split_the_bill

message = f"each person should pay : {final_payment}"
print(message)
