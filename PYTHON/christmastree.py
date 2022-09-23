def print_tree(number):

    for rows in range(number):

        right = "*"*rows
        left = " "*(number-rows)+"*"*rows

        if rows==number-1:
            print(" "*(rows+1)+"*")
        else:
            print(left+"*"+right)


print_tree(8)
