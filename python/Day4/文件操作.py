'''f=open('test1.txt','w')
f.write('hello\tworld')
f.close()'''

f=open('test1.txt','r')
con=f.read(5)
print(con)
f.close()
