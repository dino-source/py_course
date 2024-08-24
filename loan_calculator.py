# Get the loan details
msg = "How much money do you owe, in dollars?\n"  # $50,000
money_owed = float(input(msg))

msg = "What is the annual percentage rate?\n"  # 3%
apr = float(input(msg))

msg = "What is your monthly payment be, in dollars?\n"  # $1,000
payment = float(input(msg))

msg = "How many months do you want to see results for?\n"  # 24
months = float(input(msg))

# Divide apr by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr / 100 / 12

for i in range(int(months)):
    # Add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if money_owed - payment < 0:
        print("The last payment is $", money_owed)
        years = (i + 1) // 12
        months = (i + 1) % 12
        print(f"You paid off your loan in {years} years and {months} months")
        break

    # Make payment
    money_owed = money_owed - payment

    # Print the results after this month
    print("Paid", payment, "of which", interest_paid, "was interest.", end=" ")
    print("Now I owe $", money_owed, sep="")
