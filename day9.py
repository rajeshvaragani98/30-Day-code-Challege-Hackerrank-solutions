n=int(raw_input())

def factorial(n):
    if (n<=1):
        return 1 
    else:
        return n*factorial(n-1)
result=factorial(n)
print result    
