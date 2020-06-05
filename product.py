# Write a function that takes a list as an argument and returns a list where corresponding element in the output list comprises of the product
# all the elements in the input list except the current element.

# Eg: func([1,2,3]) = [2*3,1*3,1*2]

# Using division

def prod_list(lst):
    out = []
    prod = 1
    for i in range(len(lst)):
        prod *= lst[i]
    for i in range(len(lst)):
        out.append(prod//lst[i])
    return out

#print(prod_list([1, 2, 3, 4, 5]))

# Implement the function without using division

def prod_wo_division(lst):
    output = []
    def prod(lst1):
        product = 1
        for i in range(len(lst1)):
            product *= lst1[i]
        return product
    for i in range(len(lst)):
        left = lst[:i]
        right = lst[i+1:]
        prod1 = prod(left)
        prod2 = prod(right)
        ans = prod1 * prod2
        output.append(ans)
    return output

#print(prod_wo_division([1, 2, 3, 4, 5]))