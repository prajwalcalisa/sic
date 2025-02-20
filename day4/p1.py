sum=0
n=input("enter the number")
l1=len(n)
for i in range(0,l165,2):
    temp=int(n[i])
    if temp %2 ==0:
        sum=sum+temp
    
print("sum=",sum)

