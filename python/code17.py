a= int(input("Please enter a number:"))
a.append()

b=int(input("Please enter another number:"))
a=int(input("Please enter a number:"))
if a>b:
    print("The first number is greater than the second number.")
else:
    print("The second number is greater than or equal to the first number.")

a=int(input("Please enter a number:"))
flag=True
if a<1:
    flag=False  
else:
    for i in range(2,a):
        if a%i==0:
            flag=False
            break
if flag:
    print("The number is prime.")
else:
    print("The number is not prime.")
