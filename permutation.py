# Performs the permutation of all the elements in a string.
def permute(lst):
    lst1 = []
    # base case:
    if len(lst) == 1:
        return [lst]
    else:
        for i in range(len(lst)):
            main = lst[i]
            rest = lst[:i] + lst[i+1:]
            for perm in permute(list(rest)):
                lst1.append([main] + perm)
        return lst1 
#print(permute(list('abcd')))