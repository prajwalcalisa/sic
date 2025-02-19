a=[]
k=0
n=int(input("enter the number of oranges"))
for i in range(n):
    a=int(input("enter the number"))
for i in range(n):
    if a[i]<=a[n-1]:
        temp=a[i]
        a[i]=a[k]
        a[k]=temp
        k+=1
temp=a[k]
a[k]=a[i]
a[i]=temp
for i in range(n):
    print(a[i])