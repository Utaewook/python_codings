# f = open("../outputs.txt", "r")
#
# n = int(f.readline())
# size = []
# while True:
#     data = f.readline()
#     if not data:
#         break
#     size = sorted(list(map(int,data.split())))

n = int(input())
size = sorted(list(map(int, input().split())))

counts = dict()

for s in size:
    if s in counts:
        counts[s] += 1
    else:
        counts[s] = 1

print(max(counts.values()))
