n = int(input('Enter positive integer '))
sum = 0
for i in range(n):
    if (i % 2) != 0:
        sum += i
    else:
        continue
print(sum)