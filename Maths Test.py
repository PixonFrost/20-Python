# A primary school teacher wants a computer program to test the basic arithmetic skills of her students. 
# Generate random questions (2 numbers only) consisting of addition, subtraction, multiplication and division.
# The system should ask the student’s name and then ask ten questions. The program should feed back 
# if the answers are correct or not, and then generate a final score at the end.

import random as rand
import decimal
questions = []
operators = ['+', '-', '*', '/']
score = 0

def genQ():
    for i in range(10):
        num1 = rand.randrange(1,50) # generates the first number, the operater and the second number
        op = rand.choice(operators) #
        num2 = rand.randrange(1,20) #
        if op == '+':
            q = (str(num1) + " + " + str(num2)) #forms the question in a string
            ans = num1 + num2 #makes the answer as an integer
            questions.append([q, ans, 0]) #adds the question string, the answer integer and an empty third slot to a list
        elif op == '-':
            q = (str(num1) + " - " + str(num2))
            ans = num1 - num2
            questions.append([q, ans, 0])
        elif op == '*':
            num1 = rand.randrange(1,12) # just uses different numbers more suitable for multiplication
            num2 = rand.randrange(1,12) #
            q = (str(num1) + " * " + str(num2))
            ans = num1 * num2
            questions.append([q, ans, 0])
        elif op == '/':
            while True:
                num1 = rand.randrange(1,50)
                num2 = rand.randrange(1,20)
                q = (str(num1) + " / " + str(num2))
                ans = num1 / num2
                dif = (decimal.Decimal(ans)).as_tuple().exponent #gets how many decimal places
                if dif < -2:
                    pass
                elif dif >= -2: # if less than 3 places away, allows this as a question
                    questions.append([q, ans, 0])
                    break
        print(ans)

def qAnswer():
    global score
    for j in range(10):
        print("Question " + str((j + 1)) + ": " + str(questions[j][0])) #makes the question with it's number
        qAns = input("> ") 
        if float(qAns) != questions[j][1]: #if answer is incorrect
            questions[j][2] = 0
            print("Incorrect, The answer is ", questions[j][1])
        elif float(qAns) == questions[j][1]: #if correct
            questions[j][2] = 1
            score += 1
            print("Correct!")

genQ()
name = input("Please enter student name > ")
print("----------------------")
print("")
qAnswer()
print("Test finished, you scored " + str(score) + "/10")