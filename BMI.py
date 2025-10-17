# BMI Calculator Program

# Input weight and height
weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meters): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display result
print(f"Your BMI is: {bmi:.2f}")
