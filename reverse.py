# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse_string(string):
    print(string[1:])
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]

print(reverse_string("Python"))

# def reverse_string(string, result=""):
#     string1 = list(string)
#     last_char = string1.pop()
#     result = result + last_char
#     if len(string1) == 0:
#         return result
#     return reverse_string("".join(string1), result)

# print(reverse_string("Python"))

# print(reverse("")) 
# => ""
# print(reverse("a")) 
# => "a"
# print(reverse("ab")) 
# => "ba"
# print(reverse("computer")) 
# => "retupmoc"
# print(reverse(reverse("computer"))) 
# => "computer"