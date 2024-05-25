#With meters and kilograms
print("Body mass index (BMI) Calculator")

weight = float(input("Provide your weight in kilograms (ex. 70.5): "))
height = float(input("Provide your height in meters (ex. 1.70): "))


bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi,2))

if (bmi <= 18.5):
    classification = "Underweight"
elif (bmi > 18.5 and bmi <= 24.9):
    classification = "Normal Weight"
elif bmi > 24.9 or bmi <= 29.9 :
    classification = "Overweight"
else:
    classification = "Obesity"
print("The classification of your BMI is:", classification)
'''
#With pounds and inches
print("BMI (Body mass index) Calculator")

height = float(input("Provide your height in inches: "))
weight = float(input("Provide your weight in pounds: "))
#1 foot = 12 inches

bmi = (weight / (height ** 2))*703
#Fixit, IBM gets too high.

print("Your BMI is:", bmi)

if bmi < 18.5 or bmi == 18.5:
    print("You are underweight")
elif bmi > 18.5 or bmi == 24.9:
    print("You are in normal weight")
elif bmi > 24.9 or bmi == 29.9 :
    print("You are overweight")
elif bmi > 30.0 or bmi == 30.0 :
    print("You are in obesity")
else:
    print("Information is too far gone out of scale")
'''

