num=int(input("Please enter a digit: "))
numbers=[]
for i in range(num):
    n=int(input("Enter a number: "))
    numbers.append(n)
maxNumber=max(numbers)
numbers.remove(maxNumber)
print(numbers)


