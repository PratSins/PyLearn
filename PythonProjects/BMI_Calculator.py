
def BMI_calc(BMI):
    if BMI <= 18.4:
        print("You are underweight.")
    elif BMI <= 24.9:
        print("You are healthy.")
    elif BMI <= 29.9:
        print("You are over weight.")
    elif BMI <= 34.9:
        print("You are severely over weight.")
    elif BMI <= 39.9:
        print("You are obese.")
    else:
        print("You are severely obese.")

print("\n----- Welcome to Body Mass Index(BMI) Calculator Program -----\n")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height**2)
print("Your Body Mass Index is = ", bmi)
BMI_calc(bmi)
print("\n--- Thank You for using this program ---\n")