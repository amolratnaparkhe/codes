#Max subarray: Brute force method O(n^2). Not so good!
def max_subarray_brute(lst):
    lst1 = []
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            lst1.append(sum(lst[i:j]))
    return max(lst1)
lst = [-2,2,5,-11,6]
#print(max_subarray_brute(lst))

#Kadane's algortihm: To calculate the maximum subarray


def max_subarray(lst):
    current_sum = lst[0]
    max_sum = lst[0]
    for i in range(1,len(lst)):
        
        current_sum = max(lst[i],lst[i] + current_sum)
        max_sum = max(current_sum,max_sum)
        print(current_sum,max_sum)
    return max_sum

lst = [-2,2,5,-11,6]
print(max_subarray(lst))