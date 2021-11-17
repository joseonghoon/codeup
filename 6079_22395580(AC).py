a= int(input(''))
b=0

for i in range (a+1):
    b += i
    if b>=a:
        print(i)
        break
