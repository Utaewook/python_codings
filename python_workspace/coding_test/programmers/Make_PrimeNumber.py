import itertools as it

def is_prime(n):
    n_prime = True
    for i in range(2,n):
        if n%i==0:
            n_prime = False
    return n_prime

def solution(nums):
    combi = it.combinations(nums,3)
    count = 0
    for nums in it.combinations(nums,3):
        if is_prime(sum(nums)):
            count+=1
    return count