# this is a good two pointer problem to add to any list. More like a jump pointer.
# any other way of solving this problem is ... just solving it
# I eventually couldn't solve it myself but I referenced another contestants solution.

test_cases = int(input())

for idx in range(test_cases):
    string = str(input())
    startPtr = 0
    nextPtr = 0
    result_str = set()
    charIdx = 0
    while charIdx < len(string):
        while nextPtr < len(string) and string[startPtr] == string[nextPtr]:
            nextPtr += 1
        if (nextPtr - startPtr) % 2 != 0:
            result_str.add(string[startPtr])
        startPtr = nextPtr
        charIdx += 1
    sorted_string = "".join(sorted(result_str))
    print(sorted_string)
    result_str = ''
