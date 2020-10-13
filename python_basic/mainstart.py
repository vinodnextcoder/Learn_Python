# Python program to illustrate  
# function with main 
def pypart(n): 
      
    # outer loop to handle number of rows 
    # n in this case 
    for i in range(0, n): 
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ",end="") 
       
        # ending line after each row 
        print("\r") 
  
def Main(): 
    print("Started") 
    output = pypart(5)   
  
# now we are required to tell Python  
# for 'Main' function existence 
if __name__=="__main__": 
    Main() 
