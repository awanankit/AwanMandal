#take two input numbers;
a=int(input("Enter the first number: "))
b=int(input("Please enter another number"))
#check who is the greater number between two;
if(a>b):
#if a is bigger than b then
#the value of a divisible by b will be stored into the variable "div"
    div=a/b
    print("The division is: ".div)
else:
    div=b/a
    print("The division is: ".div)
    