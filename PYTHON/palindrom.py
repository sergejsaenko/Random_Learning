#"racecar" -> "racecar" = True
#"cat" -> "tac" = false

def palindrom(string):
    reverse=""
    reverse+=string[::-1]
    if reverse[0:len(reverse)] == string[0:len(string)]:
        print("True")
    print("False")

palindrom(string="cat")
