def odd_or_even(arr):
    tot=sum(arr)
    if(arr==[0]):
        return "even"
    if(tot%2==0):
        return "even"
    return "odd"