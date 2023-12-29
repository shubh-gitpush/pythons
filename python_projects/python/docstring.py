def a(n, m):
    print(n * m)


''' helllo there i am using docsting '''
n = 5
m = 8
print(a(n, m).__doc__)
#recursion
def factorial(n):
    if(n==1 or n==0):
        return(1)
    else:
        return(n*(factorial(n-1)))
print(factorial(5))
