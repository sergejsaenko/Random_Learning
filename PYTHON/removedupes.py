list=[1,1,2,3,3,3,4,5,5]
#exp: [1,2,3,4,5]

new_list=[]
for elem in list:
    if elem not in new_list:
        new_list.append(elem)
    else:
        continue
print(list)
print(new_list)