with open('DATA54.txt','r') as f:
    n,m=map(int,f.readline().split())
    a=[]
    for i in range(n):
        row=list(map(float,f.readline().split()))
        a.append(row)
print(f"{n} {m}")
for i in range(n):
    for j in range(m):
        print(a[i][j],end='     ')
    print()


for j in range(m):
    tong=sum(a[i][j] for i in range(n))
    avg=tong/n
    print(avg)