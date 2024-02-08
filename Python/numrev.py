# Reverse an integer in Python.

num = int(input())
res = 0

while(num!=0):
    res = res * 10 + num%10
    num = (num//10)

print(res)

#method 2
n = int(input())
rev = int(str(n)[::-1])
print(rev)


#method 3
def reverse(number):
    if number<10:
        return number
    else:
        return (number % 10) * 10**(len(str(number))-1) + reverse(number//10)
    

number = int(input())
print(reverse(number))