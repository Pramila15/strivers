count = 5

# Pattern 1: Solid square of asterisks
for _ in range(count):
    print('*' * count)

# Pattern 2: Right triangle of asterisks
for i in range(count):
    print('*' * (i + 1))

# Pattern 3: Numeric triangle - increasing numbers
for i in range(1, count + 1):
    print(''.join(str(j) for j in range(1, i + 1)))

# Pattern 4: Numeric triangle - repeated row number
for i in range(1, count + 1):
    print(str(i) * i)

# Pattern 5: Inverted triangle of asterisks
for i in range(count, 0, -1):
    print('*' * i)

# Pattern 6: Inverted triangle with increasing numbers
for i in range(1, count + 1):
    print(''.join(str(count - j + 1) for j in range(i)))

# Pattern 7: Pyramid of asterisks
for i in range(1, count + 1):
    print(' ' * (count - i) + '*' * (2*i - 1))

# Pattern 8: Inverted pyramid of asterisks
for i in range(1, count + 1):
    print(' ' * (i - 1) + '*' * (2*(count - i) + 1))

# Pattern 9: Diamond
# Upper half
for i in range(1, count + 1):
    print(' ' * (count - i) + '*' * (2*i - 1))
# Lower half
for i in range(1, count + 1):
    print(' ' * (i - 1) + '*' * (2*(count - i) + 1))

# Pattern 10: Triangle up then inverted
for i in range(count):
    print('*' * (i + 1))
for i in range(1, count + 1):
    print('*' * (count - i + 1))

# Pattern 11: Alternating binary pattern
for i in range(count):
    one = 1 if i % 2 == 0 else 0
    row = []
    for _ in range(i + 1):
        row.append(str(one))
        one ^= 1
    print(' '.join(row))

# Pattern 12: Palindromic numbers with spaces
for i in range(1, 5):  # count=4 as in Java example
    left = ''.join(str(j) for j in range(1, i + 1))
    spaces = ' ' * (2 * (4 - i))
    right = ''.join(str(j) for j in range(i, 0, -1))
    print(left + spaces + right)

# Pattern 13: Incremental numbers
num = 1
for i in range(1, count + 1):
    print(' '.join(str(num + j) for j in range(i)))
    num += i

# Pattern 14: Alphabet triangle
for i in range(1, count + 1):
    print(''.join(chr(ord('A') + j) for j in range(i)))

# Pattern 15: Reverse letter triangle
for i in range(1, count + 1):
    print(''.join(chr(ord('A') + (count - j)) for j in range(i)))

# Pattern 16: Repeated letters per row
alphabet = ord('A')
for i in range(1, count + 1):
    print(chr(alphabet) * i)
    alphabet += 1

# Pattern 17: Palindromic alphabet pyramid
count2 = 4
for i in range(1, count2 + 1):
    alp = ord('A')
    row = ' ' * (count2 - i)
    for j in range(i):
        row += chr(alp)
        alp += 1
    alp -= 1
    for j in range(1, i):
        alp -= 1
        row += chr(alp)
    print(row)

# Pattern 18: Incremental letters from right side
for i in range(1, count + 1):
    alp = ord('A') + count - 1
    print(''.join(chr(alp - j) for j in range(i)))

# Pattern 19: Hollow diamond-like pattern
# Upper half
for i in range(1, count + 1):
    stars = '*' * (count - i + 1)
    spaces = ' ' * (2*i - 1)
    print(stars + spaces + stars)
# Lower half
for i in range(1, count + 1):
    stars = '*' * i
    spaces = ' ' * (2 * (count - i) - 1)
    print(stars + spaces + stars)

# Pattern 20: Butterfly pattern
# Upper
for i in range(1, count + 1):
    print('*' * i + ' ' * (2*(count - i)) + '*' * i)
# Lower
for i in range(1, count):
    print('*' * (count - i + 1) + ' ' * (2*i) + '*' * (count - i + 1))

# Pattern 21: Hollow square
for i in range(1, count + 1):
    line = ''
    for j in range(1, count + 1):
        line += '*' if (i in (1, count) or j in (1, count)) else ' '
    print(line)

# Pattern 22: Numeric palindromic inverted pyramid
count2 = 4
# Upper
for i in range(1, count2 + 1):
    left = ' '.join(str(j) for j in range(count2, count2 - i, -1))
    mid = ' '.join(str(count2 - i + 1) for _ in range(2 * (count2 - i) - 1))
    right = ' '.join(str(j) for j in range(count2 - i + 2, count2 + 1))
    print((left + ' ' + mid + ' ' + right).strip())
# Lower
for i in range(count2 - 1, 0, -1):
    left = ' '.join(str(j) for j in range(count2, count2 - i, -1))
    mid = ' '.join(str(count2 - i + 1) for _ in range(2 * (count2 - i) - 1))
    right = ' '.join(str(j) for j in range(count2 - i + 2, count2 + 1))
    print((left + ' ' + mid + ' ' + right).strip())
