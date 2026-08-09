bs=int(input("Please enter a number: "))
gs=0
da=0
hra=0
if(bs>1500):
    hra=bs*10/100
    da=bs*90/100
else:
    hra=500
    da=bs*98/100
gs=bs+hra+da
print(f"Gross salary is: {gs}")