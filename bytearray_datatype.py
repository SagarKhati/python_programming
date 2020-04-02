s = 'abcd'
print(s[0])

#s[0] = '!' #TypeError: 'str' object does not support item assignment

x = b'abcd'
print(x[0])

#x[0] = 65 #TypeError: 'bytes' object does not support item assignment

#print(bytearray('abcde')) #TypeError: string argument without an encoding

print(bytearray('abcde', 'utf-8'))

x = bytearray('abcde', 'utf-8')
print(x[0])
print(x[-1])
print(x[1:4])
print(x.startswith(b'a'))

x[0] = 65
print(x)
