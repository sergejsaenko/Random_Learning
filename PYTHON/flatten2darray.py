list = [[62, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]]

empty_list=[]
for row in list:
    for col in row:
        empty_list.append(col)
print("List: ",empty_list) 