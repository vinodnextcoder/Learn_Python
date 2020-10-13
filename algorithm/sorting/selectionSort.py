# arr[] = 64 25 12 22 11

# // Find the minimum element in arr[0...4]
# // and place it at beginning
# # 11 25 12 22 64

# // Find the minimum element in arr[1...4]
# // and place it at beginning of arr[1...4]
# # 11 12 25 22 64

# // Find the minimum element in arr[2...4]
# // and place it at beginning of arr[2...4]
# # 11 12 22 25 64

# // Find the minimum element in arr[3...4]
# // and place it at beginning of arr[3...4]
# # 11 12 22 25 64 
# Python program for implementation of Selection 
# Sort 
import sys 
def SelectionSort(A): 
   for i in range(len(A)): 
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i]

    return A;
  


def Main(): 
    print("Started") 
    A = [64, 25, 12, 22, 11]; 
    print ("Sorted array") 
    output = SelectionSort(A)      
    print(output) 

# now we are required to tell Python  
# for 'Main' function existence 
if __name__=="__main__": 
    Main() 