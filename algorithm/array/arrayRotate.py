# leftRotate(arr[], d, n)
# start
#   For i = 0 to i < d
#     Left rotate all elements of arr[] by one
# end
# To rotate by one, store arr[0] in a temporary variable temp, move arr[1] to arr[0], arr[2] to arr[1] …and finally temp to arr[n-1]

# Let us take the same example arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2
# Rotate arr[] by one 2 times
# We get [2, 3, 4, 5, 6, 7, 1] after first rotation and [ 3, 4, 5, 6, 7, 1, 2] after second rotation.

# Below is the implementation of the above approach :
# Python3 program to rotate an array by  
# d elements  
# Function to left rotate arr[] of size n by d*/ 
def leftRotate(arr, d, n): 
    for i in range(d): 
        leftRotatebyOne(arr, n) 
  
# Function to left Rotate arr[] of size n by 1*/  
def leftRotatebyOne(arr, n): 
    
    temp = arr[0] 
    for i in range(n-1):
        print(arr[i]) 
        arr[i] = arr[i + 1] 
    arr[n-1] = temp 
          
  
# utility function to print an array */ 
def printArray(arr, size): 
    for i in range(size): 
        print ("% d"% arr[i], end =" ") 
  
   
# Driver program to test above functions */ 
arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7) 
printArray(arr, 7) 
