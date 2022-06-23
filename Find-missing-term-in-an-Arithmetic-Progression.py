def find_missing(sequence):
    sum=0
    length=len(sequence)
    for elem in sequence:
        sum=sum+elem
    return int(((length+1)/2)*(sequence[0]+sequence[length-1]))-sum
    
#can be optimized using the binary search into the array. 