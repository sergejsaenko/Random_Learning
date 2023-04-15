import time
import os
x = 1
i = " "*100
bar_list = [for x in range(100) print("|")]
bar="["+i+"]"

while(x != 100):
    #os.system("clear")
    bar_list[x]="|"
    print(" ".join(bar_list))
    x = x+1
    time.sleep(1)
