a=0
first=1
second=2
n=int(input("Limit:"))
q=n
while n<=2:
    if q==1:
        print(first)
        exit()
    print(a)
    a=a+1
else:
    for i in range(0,n-1):
        third=first+second
        first=second
        second=third
        print(third)
