# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

array_numbers = [2,3,4,5,-40]

def find_max(l, num = 0):
    num = l.pop()
    if num > max(l):
        return num
    return find_max(l, num)
    # Write code here

print(find_max(array_numbers))

# print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45