def bubble_sort(lst):    
    sorted_seq = False
    while sorted_seq is False: #Loop through until all the elements are sorted
        sorted_seq = True
        for i in range(len(lst)-1):           
            if lst[i] > lst[i+1]: #Checking adjacent elements in the list
                dummy = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = dummy
                sorted_seq = False
    return lst

#print(bubble_sort([3,2,1,6,4,23,11,10]))