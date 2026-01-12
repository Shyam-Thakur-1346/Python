def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter a  number:"))
print(f"the factorial of {n} is:{factorial(n)}")



def fibonacci(n):
    if(n<=1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("enter a  number:"))
print(f"the fibonacci of {n} is:{fibonacci(n)}")