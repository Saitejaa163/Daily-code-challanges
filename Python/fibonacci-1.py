num = int(input("enter series for fobinacci series: "))
first, second = 0, 1

for i in range(num):
    if i<=1:
        result = i
    else:
        result = first+second
        first = second
        second = result
    print(result, end=" ")