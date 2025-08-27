def read(self,a:int,b:int)->int:
    return a*b
a=20
for i in range (a):
    print(i,'*',a,'=',read(i,a))