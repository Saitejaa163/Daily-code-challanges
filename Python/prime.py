# Prime number

num = int(input())
factors = 0
for i in range(2,num):
    if num%i==0:
        factors += 1
        break

if factors == 1:
    print(num, " is not a Prime Number ")
else:
    print(num, " is a Prime Number")