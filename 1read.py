f=open('demo.txt','r')
# read(1) will read only 1st letter
# print(f.read(10))


# reading line by line. 
# print(f.readline())
# print(f.readline())



for i in f:
    print(i)
f.close()

