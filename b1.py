m=int(input("so dong="))
n=int(input("so cot="))
a=[]
for i in range(m):
    row=[]
    for j in range(n):
        b=int(input())
        row.append(b)
    a.append(row)
print(a)
with open('matrix.txt','w') as f:
    f.write(f"{m}  {n}\n")
    for i in a:
         f.write(" ".join(map(str, i)) + "\n")