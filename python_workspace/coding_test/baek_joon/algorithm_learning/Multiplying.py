a,b,c = map(int,input().split())

def func(val_a,val_b):
    if val_b == 0:
        return 1
    elif val_b % 2 == 1:
        return (val_a * func(val_a, val_b - 1)) % c
    else:
        half = func(val_a, val_b//2)
        return (half * half) % c


print(func(a,b))