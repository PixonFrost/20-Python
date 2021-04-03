#* basically luhns algorithm
# Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, 
# Discoverer) and validates it to make sure that it is a valid number (look into how credit cards 
# use a checksum).

# splits a string of numbers, doubles every second number, if number is two digits then adds the two digits
# together, adds new even numbers together with the odd numbers, if answer = multiple of 10 then correct

# def creditCheck(n):
#     digits = [int(x) for x in str(n)]
#     odd_digits = digits[0::2]
#     even_digits = digits[1::2] #ives every second number

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)] #separates numbers into list
    digits = digits_of(card_number) #adds numbers to a list
    odd_digits = digits[-1::-2] #gets every second number
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits) #adds all numbers in the list together
    for d in even_digits:
        checksum += sum(digits_of(d*2)) # doubles digits in list, separates new numbers and adds all together
        print(checksum)
    return checksum % 10 # finds mod 10 of the equation

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0 #checks if the mod is zero, true = valid

cardNum = input("Please enter credit card number > ")
result = is_luhn_valid(cardNum)
print(result)