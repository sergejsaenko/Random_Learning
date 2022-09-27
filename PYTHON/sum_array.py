list = [[62, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]]

#Version1
_sum=0
for row in list:
    for col in row:
        _sum+=col
print(_sum)

#Version2
_sum2=(sum(col for row in list for col in row))
print(_sum2)