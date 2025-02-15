def fun1(n):
    return n*(n+1)/2
print(fun1(4))
#THE TIME COMPLEXITY = 1
#its the most efficient
#as its complexity is the lowest


def fun2(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
print(fun2(4))
#its time complexity = n
#its linear to n
#its average case


def fun3(n):
    sum = 0
    for i in range(1,n+1):
     for j in range(1,i+1):
        sum += 1
    return sum
print(fun3(4))
#its time complexity=n^2
#its quadrec to n
#its the worst case
#its the less efficient