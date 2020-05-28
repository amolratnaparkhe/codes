def insertion_sort(lst):
    for i in range(len(lst)):
        current_value = lst[i]
        while i > 0 and current_value < lst[i - 1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    return lst
    

#print(insertion_sort([6,5,4,3,2,8,7,1]))