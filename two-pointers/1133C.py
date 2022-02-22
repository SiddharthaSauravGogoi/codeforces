test_cases = int(input())
skill_values = list(map(int, input().split()))
skill_values.sort()
counter = 1
slowPtr = 0
fastPtr = 1

for _ in range(test_cases):
    while fastPtr < test_cases and (skill_values[fastPtr] - skill_values[slowPtr]) <= 5:
        fastPtr += 1
    counter = max(counter, fastPtr - slowPtr)
    slowPtr += 1

print(counter)
