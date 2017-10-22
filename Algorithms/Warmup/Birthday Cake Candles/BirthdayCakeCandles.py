import sys


def birthdaycakecandles(n, ar):
    count = 0
    highest = max(ar)
    for i in range(0, n):
        if ar[i] == highest:
            count += 1
    return count


n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdaycakecandles(n, ar)
print(result)
