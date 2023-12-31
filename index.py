
# -------------------------------------- Assignment No 1---------------------------------------


# Exercise 01: Write a program to find the length of the variable name Variable, name=”Hello there”
name="Hello there"
print(len(name))



# Exercise 02: Write a program to find the type of the variable name 
# name=”Hello there
print(type(name))



# Exercise 03: Write a function that takes 2 numbers as arguments (age of two brothers) and find who is elder
# Hints: Use condition inside the function
def ageCompare(brother1Age, brother2Age):
    if(brother1Age>brother2Age):
        print("Brother 1 is elder")
    else:
        print("Brother 2 is elder")

print(ageCompare(30,25))
print(ageCompare(20,25))



# Exercise 04: Write a program to find the index of 7 
# numbers=[3, 5, 1, 9, 7, 2, 8 ]
numbers=[3, 5, 1, 9, 7, 2, 8 ]
print(numbers.index(7))



# Exercise 05: Write a program to sort the numbers in Ascending order
print(sorted(numbers))



# Exercise 06: Write a function named “isLandscape” that takes 2 numbers 
# (image width and height) as arguments and the function returns Landscape if the image width has a
# higher value than height. Returns Portrait otherwise
# Hints: Use condition inside the function
def isLandscape(width, height):
    if(width>height):
        return "Landscape"
    else:
        return "Portrait"

print(isLandscape(1000,1500))
print(isLandscape(2000,1500))



# Exercise 07: FizzBuzz Exercise
# Write a function that takes 1 number as argument. The function should return “Fizz” if
# the number is divisible by 3, the function should return “Buzz” if the number is divisible
# by 5, the function should return “FizzBuzz” if the number is divisible by both 5 and 3,
# otherwise return “Not a Fizz-buzz number”
# Hints: Use condition inside the function
def fizzBuzz(val):
    if(val%(3*5)==0):
        return "FizzBuzz" 
    elif(val%3==0):
        return "Fizz"
    elif(val%5==0):
        return "Buzz"
    else:
        return "Not a Fizz-buzz number"

print(fizzBuzz(27))
print(fizzBuzz(25))
print(fizzBuzz(225))
print(fizzBuzz(103))



# Exercise 08: Guessing game
# Write a function that takes a number 1 to 9 from the user input (use input function inside
# a function). Store a number in a variable (let’s assume 6). If the input value is less than
# the variable, print (your guess is almost there), if the input value is greater than the
# variable, print - your guess is higher, if the input value and variable are equals, print -
# Your Guess Is Correct!
def guessingGame(num):
    exactValue=6
    if(num<exactValue):
        print("your guess is almost there")
    elif(num>exactValue):
        print("your guess is higher")
    elif(num==exactValue):
        print("Your Guess Is Correct!")

print(guessingGame(2))
print(guessingGame(10))
print(guessingGame(6))



# Exercise 09: Find if 6 available in the list [‘4, 8, 7, 4,3,6,2,1,9’]
checkList=[4, 8, 7, 4,3,6,2,1,9]
print(6 in checkList)
