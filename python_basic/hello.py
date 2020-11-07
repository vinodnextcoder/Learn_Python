# Python program to declare variables 
myNumber = 3
print(myNumber) 
  
myNumber2 = 4.5
print(myNumber2) 
  
myNumber ="helloworld"
print(myNumber) 

princ_amount = float(input(" Please Enter the Principal Amount : "))
rate_of_int = float(input(" Please Enter the Rate Of Interest   : "))
time_period = float(input(" Please Enter Time period in Years   : "))

simple_interest = (princ_amount * rate_of_int * time_period) / 100

print("\nSimple Interest for Principal Amount {0} = {1}".format(princ_amount, simple_interest))

# Python Program to calculate Sum of Series 1³+2³+3³+….+n³
import math 

number = int(input("Please Enter any Positive Number  : "))
total = 0

total = math.pow((number * (number + 1)) /2, 2)

print("The Sum of Series upto {0}  = {1}".format(number, total))