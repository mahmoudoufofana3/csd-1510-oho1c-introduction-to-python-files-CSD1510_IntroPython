#Print a line asking the user to enter three numbers
#Prompt the user to enter the three integers, one at a time
#Display the three numbers entered, their sum, and the average.
#You can assume the user will only enter positive integers
#Example output: (you do not have to match my words exactly)
#Please enter three whole numbers:
#Number 1: 11
#Number 2: 11
#Number 3: 12
#The sum of 11 and 11 and 12 is 34 and the average is 11.333333333333334.
print("Please enter three whole numbers:")
num1 = int(input("Number 1: ")) 
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))
sum = num1 + num2 + num3
average = sum / 3
print(f"The sum of {num1} and {num2} and {num3} is {sum} and the average is {average}.")