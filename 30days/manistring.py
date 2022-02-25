s1 = 'good'

s2 = "now"

s3 = '''
nosfhslkfewr
dsfjdskf  %s
''' % s1

print(s3)

s2 = '\n\\hello, world!\\\n'
print(s2)

a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))

list1 = [1, 2, 3, 4, 5]
for i in range(len(list1)):
    print(i)

for i in list1:
    print(i)

for index, value in enumerate(list1):
    print(value)

[print(i) for i in list1]