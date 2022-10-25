n,k=input().split()
ar=list(map(int,input().split()))
y=int(k)
c=0
for i in range (0,len(ar)):
    for j in range(i+1,len(ar)):
        if (ar[i] + ar[j]) % y==0:
            c=c+1
print(c)
