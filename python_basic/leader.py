def printLeader(arr,size):
    for i in range(0,size):
        for j in range(i+1,size):
                if arr[i]<arr[j]:
                 break
        if j == size-1:
            print (arr[i])

arr=[16, 17, 4, 3, 5, 2]  
printLeader(arr, len(arr))  

## print leader
def leader(arr,size):
    maxRight=arr[size-1]
    for i in range(size-2,-1,-1):
          if maxRight <= arr[i]:         
                print (arr[i]) 
                max_from_right = arr[i] 

arr=[16, 17, 4, 3, 5, 2]  
leader(arr, len(arr))  