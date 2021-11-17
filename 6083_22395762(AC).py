r,g,b = map(int,input('').split(' '))
cnt=0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, end=' ')
            print(j, end=' ')
            print(k)
            cnt +=1
print(cnt)

