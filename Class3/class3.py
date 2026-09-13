#this is code practice for the palindrome no.

start, end = map(int, input().split())

found = False

for num in range(start, end + 1):

    if num < 0:
        continue

    if str(num) == str(num)[::-1]:
        print(num, end=" ")
        found = True

if not found:
    print("No palindrome numbers")
else:
    print()