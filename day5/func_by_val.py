def read(self,a:int)->int:
    if a<=1:return 1
    return a*self.read(a-1)
print(read(4))