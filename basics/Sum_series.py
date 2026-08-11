'''Write a Python Program to Find the Sum of the Series till the nth term:
1 + x^2/2 + x^3/3 + … x^n/n
n will be provided by the user'''

x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

sum = 1

for i in range(2, n + 1):
    sum += (x ** i) / i

print("Sum of the series =", sum)



'''Write a program to calculate the sum of series up to n term. For example, 
if n =5 the series will become 
2 + 22 + 222 + 2222 + 22222 = 24690. 
Take the user input and then calculate. 
And the output style should match which is given in the example.
'''

n = int(input("Enter the value of n: "))

sum = 0
term = 0

for i in range(1, n + 1):
    term = term * 10 + 2
    sum = sum + term

print("The sum of the series is:", sum)