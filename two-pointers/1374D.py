# had a hard time understanding this problem + let alone solve it.
# read editorial and had to reference some one else's solution to make it through

for _ in range(int(input())):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    lookup = {}
    for i in numbers:
        if i % k != 0:
            if k - i % k not in lookup:
                lookup[k - i % k] = 1
            else:
                lookup[k - i % k] += 1
    ctr = 0
    for i in lookup:
        ctr = max(ctr, i + lookup[i] * k - k+1)
    print(ctr)
