for i in range(1,11):
    for j in range (i):
        print("*",end=" ")
    print()
print('--------------------------------')
n=5
for i in range(n):
    for j in range(i):
        print(n ,end=" ")
    n-=2
    print()

print('--------------------------------')
n=5
p=0
for i in range(n):
    for j in range (i+1):
        print(p,end=" ")
    p+=2
    print()