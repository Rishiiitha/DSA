n=int(input())
a=n
d=[]
while(a!=0):
    d.append(a%10)
    a//=10
print(d)
sum=0
for i in d:
    sum+=i**3
if sum==n:print(True)
else:print(False)