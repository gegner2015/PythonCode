f=open('test.txt')

print(f.read())

print(f.read(5))

f.seek(5,0)
print(f.read())