def solve(a,x):
    new_arr=sorted(x,reverse=True)
    r_a=[new_arr[0],new_arr[1],new_arr[-2],new_arr[-1]]
    max=0
    for i in range(len(r_a)):
        for j in range(i+1,len(r_a)):
            val=abs(a-r_a[i])+abs(a-r_a[j])
            if val>max:
                max=val
    print(max)
solve(1,[3,10,10,6,5,3,7,5,1])
