# Python program to illustrate  
# function with main 
def getInteger(): 
    result = int(input("Enter integer: ")) 
    return result 
  
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