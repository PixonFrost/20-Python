# A happy number is defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits, and 
# repeat the process until the number equals 1 (where it will stay), or it loops endlessly
# in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, 
# while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find the 
# first eight happy numbers

def digits_of(n):
    return [int(d) for d in str(n)] #separates num
def square(list):
    return [i ** 2 for i in list] #squares each num in list

num = input("> ")
while True:
    num = sum(square(digits_of(num))) #separates number, square's each, adds together
    if num == 1:
        break
    else:
        pass
print("True")