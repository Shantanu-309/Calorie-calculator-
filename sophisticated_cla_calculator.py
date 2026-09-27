print("calorie calc to find out your current body baseline")
print("\n")

Weight = float(input("Your weight in kg: "))
height = float(input("your height in cm: "))
age = int(input("how old are you: "))
gender = input("your gender (male/female): ").strip().lower()
activity = int(input("How active are you on a scale of 1 to 5, 1 being the least active and 5 being the most: "))

Bmi = Weight / ((height * 0.01) ** 2)

if Bmi < 18.5:
    bmi_category = "Underweight"
elif Bmi < 25:
    bmi_category = "Healthy weight"
elif Bmi < 30:
    bmi_category = "Overweight"
elif Bmi < 35:
    bmi_category = "Obesity - Class I"
elif Bmi < 40:
    bmi_category = "Obesity - Class II"
else:
    bmi_category = "Obesity - Class III"

if gender == "male":
    Bmr = 10 * Weight + 6.25 * height - 5 * age + 5
elif gender == "female":
    Bmr = 10 * Weight + 6.25 * height - 5 * age - 161
else:
    print("Invalid gender input")
    exit()

activity_multipliers = {
    1: 1.20,
    2: 1.375,
    3: 1.55,
    4: 1.725,
    5: 1.90,
}

if activity not in activity_multipliers:
    print("Invalid activity level, please enter a number from 1 to 5")
    exit()

tdee = Bmr * activity_multipliers[activity]

print("\n")
print("========================================")
print("          CALORIE CALCULATOR")
print("========================================")

print("\nBODY INFORMATION")
print("----------------------------------------")
print(f"Weight:       {Weight} kg")
print(f"Height:       {height} cm")
print(f"Age:          {age}")
print(f"Gender:       {gender.capitalize()}")

print("\nBMI")
print("----------------------------------------")
print(f"BMI:          {Bmi:.2f}")
print(f"Category:     {bmi_category}")

print("\nCALORIE ESTIMATES")
print("----------------------------------------")
print(f"BMR:          {Bmr:.0f} kcal/day")
print(f"Maintenance:  {tdee:.0f} kcal/day")

print("\nGOALS")
print("----------------------------------------")
print(f"Mild loss:    {tdee * 0.89:.0f} kcal/day")
print(f"Weight loss:  {tdee * 0.78:.0f} kcal/day")
print(f"Extreme loss: {tdee * 0.56:.0f} kcal/day")

print("\n========================================")
