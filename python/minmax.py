a=int(input("Please enter a number: "))
num=[]
for i in range(a):
    p=int(input("Please enter a number: "))
    num.append(p)
    maxnum=max(num)
    mininum=min(num)
    sum=maxnum+mininum
print(sum)
