weight=int(input())
hight=float(input())

BMI= weight/hight**2
print(BMI)
if(BMI<18.5):
    print("YOU are underweight")
elif(BMI>= 18.5 and BMI<25):
    print("normal weight")
elif(BMI>= 25 and BMI<30):
    print("over wigtht")
else:
    print("elinically")
