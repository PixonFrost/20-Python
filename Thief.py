#A thief has managed to find out the four digits for an online PIN code, but doesn’t know the correct 
# sequence needed to hack into the account.
#Design and write a program that displays all the possible combinations for any four numerical digits 
# entered by the user. The program should avoid displaying the same combination more than once.

from itertools import permutations
n = input("Please enter a 4 digit number > ")
digits = [int(x) for x in str(n)] # separates the number into 4 digits

for subset in permutations(digits, 4): #for each 4 digit combo in list
    print(subset)
