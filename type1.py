a=[1,23,89,12,15,6,3]
b=[5,16,23,95,65]
def swap(z,x,y):
    num1 = z[x]
    num2 = z[y]
    z[y]=num1
    z[x]=num2
    return z
print(swap(b,0,-1))