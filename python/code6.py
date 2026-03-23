a=int(input("Enter a school marks between 0 and 100: "))
if a>=90 and a<=100:
    print("Your grade is A")
elif a>=80 and a<90:
    print("Your grade is B")
elif a>=70 and a<80:
    print("Your grade is C")
elif a>=60 and a<70:
    print("Your grade is D")
else:
    print("Your grade is F")