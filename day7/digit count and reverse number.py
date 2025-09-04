a=int(input())
b=a
c=0
new=0
while(b!=0):
    b//=10
    c+=1
print(c)
for i in range(c):
    new=new*10+a%10
    a=a//10
print(new)