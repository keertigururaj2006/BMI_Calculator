# BMI Calculator with Category Display

# Input weight and height
weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meters): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display BMI value
print(f"Your BMI is: {bmi:.2f}")

# Determine and display BMI category
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 25:
    print("Category: Normal weight")
else:
    print("Category: Overweight")
