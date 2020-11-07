my_list = [2,1,4,5]
new_list = []

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)    

# for i in range (Number):
#     for j in range(i + 1, Number):
#         if(NumList[i] > NumList[j]):
#             temp = NumList[i]
#             NumList[i] = NumList[j]
#             NumList[j] = temp

print(new_list)