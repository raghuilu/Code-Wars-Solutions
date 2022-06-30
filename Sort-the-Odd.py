def sort_array(source_array):
    # Return a sorted array.
    arr=sorted([num for num in source_array if num %2 ==1 ])
#     print(arr)
    for i,im in enumerate(source_array):
        if im%2==0:
            arr.insert(i,im)
#         print(arr)
    return arr