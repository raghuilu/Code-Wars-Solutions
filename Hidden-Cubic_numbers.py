import re
def is_sum_of_cubes(s):
    res=''
    sA=[0]
    for nums in list(re.findall('[0-9]{1,3}', s)):
        cubic=sum(list(map(lambda x: int(x)**3, list(nums))))
        if nums==str(cubic):
            res+=str(nums)+' '
            sA.append(int(nums))
    print(res)
    print(sum(sA))
    if res:
         return res+ str(sum(sA))+' Lucky'
    return "Unlucky"