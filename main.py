print("Enter the first no.: ")
a = int(input())
print("Enter the second no.: ")
b = int(input())
print("Enter the third no.: ")
c = int(input())

# problem 1
ctr = product = 0
ctr = int(b)
while (ctr != 0):
    product = product + int(a)
    ctr = ctr - 1

print("1) The product of ", a, " and ", b, " is ", product)

# problem 2
factorial = 1
ctr = a
while (ctr != 0):
    factorial = ctr * factorial
    ctr = ctr - 1

print("2) ", a, " is ", factorial)

