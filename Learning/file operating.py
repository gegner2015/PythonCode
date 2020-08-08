f=open('test.txt')

print(f.read())

print(f.read(5))

f.seek(5,0)
print(f.read())

f.close();

f=open('test.txt','r+')

f.seek(0,2)

f.write('i love you')

f.close()

f=open('test.txt','a')

f.write('i hate you \n')

f.write('i love you')

f.close()

f=open('test.txt')
print(f.read())

