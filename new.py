def factorial(n):
    fact=1
    if n==0 :
        return fact
    else:
        fact=n*fact
        n=n-1
        return factorial(n)*fact
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
        
    
print(factorial(5))  
print(sum(4))  