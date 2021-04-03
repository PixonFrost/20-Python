#The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and 
# the factorial of zero, 0, is defined as being 1. Solve this using both loops and recursion.

num1 = int(input("Please enter a number > "))
num3 = num1

for i in range(1, num1): #repeats num1 times
  num2 = num1 - i #takes the amount of times it has repeated away from num1
  num3 = num3 * num2
  print(num3)