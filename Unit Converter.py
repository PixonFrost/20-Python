# Converts various units between one another. The user enters the type of unit being entered, the type 
# of unit they want to convert to and then the value. The program will then make the conversion

#* Celcius to F = * 9 / 5 + 32
#* F to C = - 32 * 5 / 9

#* GBP to USD = * 1.4
#* USD to GBP = / 1.4
loop = True
while loop == True:
    print("""Please enter the type you want to convert, followed by the type you want to convert to and then the amount you wish to convert
    Cel to Far | Far to Cel
    GBP to USD | USD to GBP
    """)
    print

    convert1 = input("1st > ")
    convert2 = input("2nd > ")
    convert3 = int(input("num > "))

    #* temperature
    if (convert1.lower() == "c"):
        if (convert2.lower() == "f"):
            convert4 = convert3 * 9 / 5 + 32
            print(str(convert4) + "f")
            loop = False
    elif (convert1.lower() == "f"):
        if (convert2.lower() == "c"):
            convert4 = convert3 - 32 * 5 / 9
            print(str(convert4) + "c")
            loop = False

    #* currency
    elif (convert1.lower() == "gbp"):
        if (convert2.lower() == "usd"):
            convert4 = convert3 * 1.4
            print("$" + str(convert4))
            loop = False
    elif (convert1.lower() == "usd"):
        if (convert2.lower() == "gbp"):
            convert4 = convert3 / 1.4
            print("£" + str(convert4))
            loop = False