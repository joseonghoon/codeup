n = int(input(''))
s=0

for i in range(0,n+1):
    s += i
    if s>=n:
        break

print(s)
