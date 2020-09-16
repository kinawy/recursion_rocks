# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n, result=0):
    result = result + n
    n-=1
    
    # Base
    if n == 0:
        return result

    return factorial(n, result)

print(factorial(5))

# print(factorial(5))
# => 120