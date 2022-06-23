def get_middle(s):
    #your code here
    lens=len(s)
    print(lens)
    if(lens%2>0):
        return s[int(lens/2)]
    if(len(s)%2==0):
        return (s[int((lens / 2 )- 1): int((lens / 2) + 1)])
    else:
        return s