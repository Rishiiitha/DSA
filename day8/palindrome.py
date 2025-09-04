s=input()
n=len(s)
k=[]
r=True
for i in range(n):
    if s[i].isnumeric() or s[i].isalpha():k.append(s[i].lower())
n=len(k)
if(n%2==0):m=n//2
else:m=(n+1)//2
print(k)
for i in range(m):
    if k[i]!=k[n-i-1]:r= False
print(r)
        