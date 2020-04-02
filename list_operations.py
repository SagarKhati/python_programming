emplist1 = list()
print(emplist1)

emplist1.append(9)
emplist1.append(10)
print(emplist1)

emplist2 = []
print(emplist2)
emplist2.extend('abc')
print(emplist2)

e = emplist2.pop(len(emplist2)-1)
print(emplist2)
print(e)
