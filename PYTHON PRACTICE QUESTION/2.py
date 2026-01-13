#Write a function to calculate the sum of first N natural numbers.

def sum(n):
    if(n==1):
        return 1
    elif(n==0):
        print("0 is not a natural number")
    else:
        return n+sum(n-1)
print(sum(5))