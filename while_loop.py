total = 0
i = 0
while i<10:
    total = total + i
    print(total)
    i = i + 1



s = 'tata consultancy services limited'
i = 0
count = 0
while i < len(s):
    if s[i] in ['a', 'e', 'i', 'o', 'u']:
        count = count + 1
    i = i + 1
print(count)
