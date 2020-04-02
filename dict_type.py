a = {'john':15000, 'mac':20000}
print(a['john'])
print(a['mac'])

a['john'] = 90000
print(a['john'])

del a['mac']
print(a)

a['ramesh'] = 12300

print(a.keys())
print(a.values())

d1 = dict()
print(d1)

d2 = {'p':'play', 't':'talk'}
print(d2)

d2['v'] = 'vibes'
d2['d'] = 'docs'
print(d2)

del d2['v']
print(d2)
