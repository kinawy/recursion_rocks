# # You will have to figure out what parameters to include
# # 🚨 All functions must use recursion 🚨`

# # This function returns an array of all possible outcomes from flipping a coin N times.
# # Input type: Integer 
# # H stands for Heads and T stands for tails
# # Represent the two outcomes of each flip as "H" or "T"

# def coin_flips(n):
#     # Write code here
#     pass

# # print(coinFlips(2)) 
# # => ["HH", "HT", "TH", "TT"]

# Current starts with empty string
# Begin with empty results
def addFlips(n, result=[], current=''):
    if (n == 1): 
        # This is the last flip, so add the result to the array
        result.append(current + 'H')
        result.append(current + 'T')
    else: 
        # Let's say current is TTH (next combos are TTHH and TTHT)
        # Then for each of the 2 combos call add Flips again to get the next flips.
        addFlips(n - 1, result, current + 'H')
        addFlips(n - 1, result, current + 'T')
    return result

print(addFlips(1))