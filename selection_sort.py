def selection_sort(lst):
    for i in range(len(lst)-1):  # Not going till the last element
        min_index = i
        for j in range(i+1,len(lst)): #starting one after to compare with the min value from the parent loop
            if lst[j] < lst[min_index]:
                min_index = j
        # Do the swap here!
        if min_index != i:
            lst[min_index],lst[i] = lst[i], lst[min_index]
        #print(lst) Just for testing and checking for the patterns!
    return lst

#print(selection_sort([5,4,3,7,2,1,6,9,8]))
