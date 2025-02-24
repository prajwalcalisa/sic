sum=0
n=input("enter the number")
l1=len(n)
for i in range(0,l1,2):
    temp=int(n[i])
    sum=sum+temp
print(sum)

