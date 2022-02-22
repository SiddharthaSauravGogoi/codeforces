for _ in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))
    if n < 4:
        print(*numbers)
    else:
        first = 0
        last = n - 1
        while first < last:
            print(numbers[first], numbers[last], end=' ')
            first += 1
            last -= 1
        if n % 2 == 1:
            print(numbers[first], end='')
