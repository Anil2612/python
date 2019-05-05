a=[]
j=0
print("Enter the size of array:",end="")
n=int(input())
print("Elements:")
for i in range(0,n):
    j=j+1
    print(j, ": ",end="")
    b=input()
    a.append(int(b))
for item in a:
    print(" ",item,end="")

print("\n")

for i in range(0,n):
    for j in range(0,n-i-1):
        if a[j]<a[j+1] :
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t

for item in a:
    print(" ",item,end="")
