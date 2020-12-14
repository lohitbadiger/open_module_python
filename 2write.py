
# write will replace the existing content and adds the new content

f=open('demo.txt', 'w')
f.write('i  have no job')

f.close()
f=open('demo.txt','r')
print(f.read())
