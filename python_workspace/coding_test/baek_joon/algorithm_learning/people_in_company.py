n = int(input())

system = dict()
for _ in range(n):
    name, log = input().split()
    if log == 'enter':
        system[name] = 1
    else:
        del system[name]

for name in sorted(system.keys(), reverse=True):
    print(name)