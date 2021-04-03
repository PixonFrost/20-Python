# This is a tool that allows the user to enter a text string and then in a separate text box enter a 
# regex pattern. It will run the regular expression against the string and return any matches or flag 
# errors in the regular expression

import re
txt = input("Please enter text string > ")
reExpress = input("Please enter a word to find > ")
print(re.findall(reExpress, txt)) 

#? i don't know what it wants me to do