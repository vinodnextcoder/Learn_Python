# Python program to illustrate  
# function with main 
def getInteger(): 
    a=int(input("Enter value of first variable: "))
    b=int(input("Enter value of second variable: "))
    a=a+b
    b=a-b
    a=a-b
    print("a is:",a," b is:",b)
    return a
  
def avgNumber():
    n=int(input("Enter the number of elements to be inserted: "))
    a=[]
    for i in range(0,n):
        elem=int(input("Enter element: "))
        a.append(elem)
    avg=sum(a)/n
    print("Average of elements in the list",round(avg,2))
def Main(): 
    print("Started") 
  
    # calling the getInteger function and  
    # storing its returned value in the output variable 
    output = getInteger()      
    print(output) 
    avgNumber()
  
# now we are required to tell Python  
# for 'Main' function existence 
if __name__=="__main__": 
    Main() 