n, t = map(int, input().split())
book_timings = list(map(int, input().split()))

total_books_read = 0
leftPtr = 0

for time in range(0, len(book_timings)):
    total_books_read += book_timings[time]
    if total_books_read > t:
        total_books_read -= book_timings[leftPtr]
        leftPtr += 1

print(len(book_timings) - leftPtr)
