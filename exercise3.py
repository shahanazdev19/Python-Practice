#-----------------------Exercise 3-----------------------------

# 1:
# Take user input in python. Add two numbers from the input, and also add two strings to
# understand formats in python

numValue1=int(input("Enter first number "))
numValue2=int(input("Enter second number "))
sum=numValue1+numValue2

strValue1=input("Enter a string value ")
strValue2=input("Enter another string value ")
concatStr=strValue1+" "+strValue2

print(f"The sum of two number {numValue1} and {numValue2} is {sum}")
print(f"Concatenation of two string {strValue1} and {strValue2} is '{concatStr}'")

# 2:
# Create a list of products, using dictionary values, like:
# [{category: cars, brand: porsche, model: 911 GT}, …] and use stack operations to print
# values from this list.

dicList=[{'category': 'cars', 'brand': 'porsche', 'model': '911 GT'},
         {'category': 'Motor Cycle', 'brand': 'Honda', 'model': '1234'}]

for _ in range(len(dicList)):
   dic=dicList.pop()
   itemDetails=[]
   for item in dic.items():
     itemDetails.append(': '.join(item))
   print(", ".join(itemDetails))
# or
while dicList:
   dic=dicList.pop()
   for key, val in dic.items():
     print(f"key: {key} and value: {val}")
# or
for x in dicList[::-1]:
   dic=dicList.pop()
   for key, val in dic.items():
     print(f"key: {key} and value: {val}")
        
# 3:
# Given a list of tuples of the shape (Name, roll, marks), write python code to sort this list
# according to marks in descending order. (try to use lambda function)
# I.e: [(‘kafka, 1, 83), (‘orwell’, 2, 70), (‘hemingway’, 3, 95), …]
tupleList=[("kafka", 1, 83), ("orwell", 2, 70), ("hemingway", 3, 95)]
sorted_list=sorted(tupleList,key=lambda x:x[2])
print(sorted_list)


# 4:
# Write a recursive function to reverse a string in python
def count(n):
    print(n)
    if(n==0): 
        return
    else:
        count(n-1)
print(count(10))

# 5:
# Write a recursive function to calculate the n-th fibonacci number
def recursion_factorial(x): 
    if x == 1:
        return 1
    else:
        return (x * recursion_factorial(x-1))
num = 6
print(f"The recursion result of factorial {num} is {recursion_factorial(num)}")