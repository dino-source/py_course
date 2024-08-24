start = 10
stop = 21
step = 2

sum = sum(range(start, stop, step))

for x in range(start, stop, step):
    print(x)

print("You spent $", sum, " on lunch this week.", sep='')
