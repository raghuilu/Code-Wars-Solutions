from asyncio.events import BaseDefaultEventLoopPolicy
from hashlib import new
from heapq import merge
from logging import root
from platform import node
from sys import prefix


def f(n):  
    memo = [0] * (n+1)  
    memo[0], memo[1] = 0, 1  
    for i in range(2, n+1):   
        memo[i] = memo[i-1] + memo[i-2] 
    return memo[n-1]
# print(f(5))
# Too simple Iterative Approach


# Dymanamic programming process:
# Step1: Identify the subproblem in Words
# step2:Write out the sub-problem as a recurring mathematical decision.
# What about the other steps?
# Working through Steps 1 and 2 is the most difficult part of 
# dynamic programming. 
# As an exercise, I suggest you work through Steps 3, 4, and 5 on 
# your own to check your understanding.
# Generally, a dynamic program’s runtime is composed of the following features:

# Pre-processing
# How many times the for loop runs
# How much time it takes the recurrence to run in one for loop iteration
# Post-processing
# Overall, runtime takes the following form:

# Pre-processing + Loop * Recurrence + Post-processing
# length of increasing subsequence problem
def lis(a):
    l=[1]*len(a)
    for i in range(1,len(l)):
        subproblems=[l[k] for k in range(i) if a[k]<a[i]]
        l[i]=1+max(subproblems,default=0)
    return max(l,default=0)
# print(lis([5,2,8,6,3,6,9,5]))
arr=[0,1,2,2,1,0]
# print(sorted(arr))
def solve(a,x):
    new_arr=sorted(x,reverse=True)
    r_a=[new_arr[0],new_arr[1],new_arr[-2],new_arr[-1]]
    max=0
    print(r_a)
    for i in range(len(r_a)):
        for j in range(i+1,len(r_a)):
            val=abs(a-r_a[i])+abs(a-r_a[j])
            # print(abs(a-r_a[i]))
            # print(abs(a-r_a[j]))
            # print(val)
            if val>max:
                max=val
    print(max)
# solve(1,[3,10,10,6,5,3,7,5,1,])
# def g_c(n,a):
#     new_arr=sorted(a)
#     print(new_arr)
# g_c([1,3,5,2,1,1])
# from binarytree import *
# nodes=[1,2,3,4,5,6,7,8,9,10]
# tree=bst()
# print(bst())
def split(a):
    return int(str(a)[0]+str(a)[1]),int(str(a)[2]+str(a)[3])
def karatsuba_mul(a,b):
    aF,aS=split(a)
    bF,bS=split(b)
    step1=aF*bF
    print(step1)
    step2=aS*bS
    print(step2)
    step3=(aF+aS)*(bF+bS)
    print(step3)
    step4=step3-step1-step2
    print(step4)
    answer=step1*(10**4)+step2+step4*(10**2)
    print(answer)
# mul(5678,1234)
#making a recursive case should be interesting. 
#let's do this shit
def k_m(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        nby2 = n / 2
        a = x / 10**(nby2)
        b = x % 10**(nby2)
        c = y / 10**(nby2)
        d = y % 10**(nby2)
        ac = k_m(a,c)
        bd = k_m(b,d)
        ad_plus_bc = k_m(a+b,c+d) - ac - bd
        prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
        return prod
# print(k_m(1234,5678))
#  maximum recursion depth exceeded while getting the str of an object
def merge_sort(a):
    if len(a)>1:
        left=a[:len(a)//2]
        right=a[len(a)//2:]
        merge_sort(left)
        merge_sort(right)
        i=0
        j=0
        k=0
        while i< len(left) and j <len(right):
            if(left[i]<right[j]):
                a[k]=left[i]
                i+=1
            else:
                a[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            a[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            a[k]=right[j]
            j+=1
            k+=1
        print(a)
# merge_sort([4,2,1,3])
ini=["welcome","to","turing"]
print(ini)
for i in ini:
    ini.append(i.upper())
print(ini)