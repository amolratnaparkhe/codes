# Mergesort implementation

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        midpoint = len(lst)//2
        left = merge_sort(lst[:midpoint])
        right = merge_sort(lst[midpoint:])
        output = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                output.append(left[0])
                del left[0]
            else:
                output.append(right[0])
                del right[0]
        output.extend(left)
        output.extend(right)
    return output

#print(merge_sort([3,2,1,5,7,9,6,12,4]))