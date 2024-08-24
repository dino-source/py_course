total = 0
expenses = []
number_of_expenses = int(input("Enter number of expenses: "))
for i in range(number_of_expenses):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)
print("You spent $", total, sep='')
