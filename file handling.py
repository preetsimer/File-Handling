
#Question 1
f=open('test.txt')
lines=f.readlines()
x=int(input("Enter number of lines to read: "))
for i in range(x):
    print(lines[i])
f.close()



#Question 2
li=[]
dic={}
f=open('test2.txt')
data=f.read()
li=(data.split())
for i in li:
    dic[i]=li.count(i)
print("The frequency of each word in the file is :")
print(dic)
f.close()


#Question 3
f=open('test1.txt')
g=open('test2.txt','w')
data=f.read()
g.write(data)
g.close()
g=open('test2.txt')
data2=g.read()
print(data2)
g.close()
f.close()


#Question 4
with open('test1.txt') as f1,open('test2.txt') as f2 ,open('combine.txt','w') as f3:
    for i,j in zip(f1,f2):
        f3.write(i+j)
f=open('combine.txt')
data=f.read()
print(data)

#Question 5
li=[]
f=open('test3.txt','w')
print("Enter 10 number in the file: ")
for i in range(10):
    n=input()
    f.write(n)
    f.write('\n')
f.close()
f=open('test3.txt')
data=f.read()
data2=data.split()
for i in data2:
    li.append(int(i))
li.sort()
data3=','.join(map(str,li))
f2=open('test4.txt','w')
f2.write(data3)
f2.close
f2=open('test4.txt')
data4=f2.read()
print("The Sorted Numbers are :")
print(data4)



