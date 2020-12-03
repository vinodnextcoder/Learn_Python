def isMajority(a): 
      
    # Insert all elements  
    # in a hash table 
    mp = {} 
      
    for i in a: 
        if i in mp:
            print(mp[i])
            mp[i] += 1
        else:
            mp[i] = 1
      
    # Check if frequency  
    # of any element is 
    # n/2 or more. 
    for x in mp: 
        if mp[x] >= len(a)//2: 
            return True
    return False
  
# Driver code 
a = [ 2, 3, 9, 2, 2 ] 
  
print("Yes" if isMajority(a) else "No")