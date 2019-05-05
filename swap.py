def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print("*****")
    print("a=",end="")
    print(a)
    print("b=",end="")
    print(b)


a=input("Enter first number:")
b=input("Enter second number:")
print("\n*****")
print("a=",end="")
print(a)
print("b=",end="")
print(b)
swap(int(a),int(b))
print("*****")
