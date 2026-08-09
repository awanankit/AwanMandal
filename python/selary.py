ds=int(input("Please enter the salary: "))
gs=0
da=0
hra=0
if (ds>1500):
    hra=ds*10/100
    da=ds*90/100
else:
    hra=500
    da=ds*98/100
gs=ds+hra+da
print(f"Gross salary is: {gs}")