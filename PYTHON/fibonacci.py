

def fib(n):
    count=0
    n1,n2=0,1
    while count <n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
    
    
n=100
fib(n)