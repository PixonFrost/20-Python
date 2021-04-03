# Show how to spell out a number in English. You can use a pre-existing implementation or make your own, 
# but you should support inputs up to at least one million (or the maximum value of your language’s 
# default bounded integer type, if that’s less)

from num2words import num2words
num = input("Please input a number > ")
print(num2words(num, lang='en_GB'))