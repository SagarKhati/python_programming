a = ["banana", "apple", "microsoft"]
for element in a:
    print(element)

for element in a:
    print(element)
    print(element)

b = [20, 10, 5]
for e in b:
    print(e)

total = 0
for e in b:
    total = total + e
print(total)

c = list(range(1,5))
print(c)

for i in range(1, 5):
    print(i)

total2 = 0
for i in range(1, 5):
    total2 += i
print(total2)

print(list(range(1, 8)))

print(5 % 3)
print(1 % 3)
print(6 % 3)

total3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total3 += i
print(total3)

# all multiples of 3,5 that are less than 100
for i in range(100):
    if i%3==0 or i%5==0:
        print(i)


s = 'tata consultancy services limited'
count = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        count += 1
print(count)
