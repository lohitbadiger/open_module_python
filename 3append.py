# append will add the new content at the end

f=open('demo.txt','a')

f.write('now i will search for new one')
f.write('\nadded 3 times now i will search for new one')

f.close()

f=open('demo.txt','r')
print(f.read())
