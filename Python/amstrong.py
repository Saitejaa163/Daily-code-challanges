# Amstrong Number

num = int(input())
value = 0
temp = num

count = len(str(num))

while(temp > 0):
    digit = temp % 10
    value += digit ** count
    temp = temp//10

if num == value:
    print(num, " is an Amstrong Number....!! ")
else:
    print(num, " is not an Amstrong Number")


#Method 2
    
number = int(input())
digits = [int(digit) for digit in str(number)]
count = len(digits)
total = sum([digit ** count for digit in digits])

if number == total:
    print(number, " is an Amstrong Number....!! ")
else:
    print(number, " is not an Amstrong Number")
