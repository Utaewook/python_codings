a,b = map(int,input().split())
m = int(input())

h, m = (a+(m+b)//60)%24, (b+m)%60

print(h,m)