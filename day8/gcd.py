def read(a:int,b:int)->int:
    if a%b==0:return b
    return read(b,a%b)
a=int(input())
b=int(input())
print(read(a,b))
