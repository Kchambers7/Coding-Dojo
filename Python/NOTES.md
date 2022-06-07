Python ( python3 to run file in terminal )

You don't have to use var and num for stuff you can just type it...

Basically everything in Python is an object 

-A code block is a set of lines of code that- belong together. For example, the first line of an if statement gives the condition, but the line(s) that follow explain what we want to happen if the condition is true.

EX:def (functions)
if, elif, else (conditional statements)
for, while (loops)
Class (classes)

-Python has provided us with the pass statement- for situations where we know we need the block statement, but we aren't sure what to put in it yet.

-class EmptyClass:
    pass

-for val in my_string:
    pass


*when adding strings in Python*


EX: print("I love to eat", fave_food )

you can add by using append


LOOPS (start, stop, step)






* FUNCTIONS * 
my_func 

- if  a function doesnt return anything it will return "none" my default 




* CLASSES *
 when keeping track of a user you can use class keyword to define it. If you want to add a user for example you would do adrian = User()

class User:
    
    def _init_(self, name, email, password):
      self.name = name
      self.email = email
      self.password = password 
      self.account_balance = 0


    def deposit(self, amount:
      self.account_balance += amount

      def withdrawl(self, amount):
      self.account_balance += amount

    adrian = User("Adrian", "adog@aol.com, "handsomcoder123")
    tyler = User ("Tyler", "tmax@gmail.com", "luvcats")


print(adrian)
print(tyler)

priny(dir(adrian))



* METHODS
  - 


* ALGORITHMS *

#print sum of 0-255
#print integers from 0 to 255, and which each integer print the sum so far. 

sum = 0 
for i in range (256)
sum = sum + i 


# Find and Print Max
# Given an array, find and print its largest element.

test_array = [1,2,3,4,5,6,7,255]

def printMax(theArrayParam):
   max = theArrayParam[0]
   for i in theArrayParam:
     if(i > max):
      max=i 
    print(max)

printMax(test_array)

(notes) you must stay in the for loop when doing the forloop

# Array with Odds
# Create an array with all the odd integers between 1 and 255 (inclusive).

oddList = []
   for i in range(1,256)
   if(i % 2 != 0)
     oddList.append(i)
print(oddList)

(notes) - 

# Greater Than Y
# Given an array and a value Y, count and print the number of array values greater than Y.

test_array = [1,2,3,4,5,6,7,255]
test_array1 = [1,2,3,4]

def greaterThanY(arrParam, yParam):
     count = 0
     for i in arrParam: 
          if(i > yParam):
            count += 1

     greaterThanY(test_array1,1)


(notes)- arrParam = array 
yParam = Y 
if you want to count something its (count= whatever # you're using)

# Max, Min, Average
# Given an array, print the max, min and average values for that array.
  def maxMinAvg(arrParam):
        max = arrParam[0]
        min = arrParam[0]
      for i in arrParam:
       sum += i 
        if(i > max):
         max=i 
    if(i < min):
    min = 1
    print(max,min,sum/len(arrParam))

    maxMinAvg(testarray)


    * Find Sum Of ODD numbers From 1 to N * 
Use the following steps to find or calculate sum of odd number from 1 to n in python:

- Take the input number from 1 to that user-entered value
- Define a variable, which name total
- Iterate for loop and check each number using num%2 != 0 formula is it odd or not.
- If the number is odd, so add the number into total variable
- Print the sum of odd number

maximum = int(input(" Please Enter the Maximum Value : "))
Oddtotal = 0
 
for number in range(1, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number
 
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Oddtotal))


* Find Sum of EVEN numbers from 1 to N * 
  - Take the input number from 1 to that user-entered value
- Define a variable, which name total
- Iterate for loop and check each number using num%2 == 0 formula is it even or not.
- If the number is even, so add the number into total variable
- Print the sum of even number

# Python Program to Calculate Sum of Even Numbers from 1 to N
  
maximum = int(input(" Please Enter the Maximum Value : "))
total = 0
 
for number in range(1, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))
        total = total + number
 
print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, total))




# Swap String For Array Negative Values
# Replace any negative array values with 'Dojo'.

