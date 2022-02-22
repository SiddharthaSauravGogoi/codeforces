n, m = map(int, input().split())
dorms = list(map(int, input().split()))
rooms = list(map(int, input().split()))
sum = 0
idx = 0

for element in rooms:
    while element > sum:
        sum = sum + dorms[idx]
        idx += 1
    print(idx, element - (sum - dorms[idx - 1]))
