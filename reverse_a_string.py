#Using for loop
inputStr = 'Geeksforgeeks'
result = ''
for i in range(len(inputStr)-1, -1, -1):
    result = result + inputStr[i]
print(result)

#Using reversed() function
inputStr = 'Geeksforgeeks'
reversedChars = reversed(inputStr)
print(''.join(reversedChars))

#Using extended slicing
inputStr = 'Geeksforgeeks'
print(inputStr[-1::-1])
