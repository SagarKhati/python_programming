import sys

x = input("Enter 1st number : ")
y = input("Enter 2nd number : ")
z = x + y
print(z)

x = input("Enter 1st number : ")
a = int(x)
y = input("Enter 2nd number : ")
b  = int(y)
z = a + b
print(z)

x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))
z = x + y
print(z)

ch = input('Enter a char : ')
print(ch)

ch = input('Enter a char : ')
print(ch[0])

ch = input('Enter a char : ')[0]
print(ch)

result = eval(input("Enter an expression : "))
print(result)

#command line arguments
x = sys.argv[1]
y = sys.argv[2]
z = x + y
print(z)
