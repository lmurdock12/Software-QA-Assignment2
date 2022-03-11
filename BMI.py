def get_user_input():
    """ 
    Get the user's body measurements
    
        Returns a tuple of: (height in feet, remaining height in inches, weight in lbs)
    """
    #Input height in feet
    #Input rest of height in inches
    height_feet = int(input("Please enter your height in feet: "))
    height_inches = int(input("Please enter your remaining height in inches: "))

    #Input weight in lbs
    weight = int(input("Please enter your weight in pounds: "))

    return (height_feet,height_inches,weight)


def calculateBMI(feet,inches,weight):
    """ 
    Calculate the BMI based off the user's measurements
    
        Returns BMI as a float
    """
    # 1. Convert weight to kgs (multiply by .45)
    weight_KG = weight * .45

    # 2. Convert height to total inches and multiple by 0.025 (conversion factor)
    total_inches_CM = (feet*12 + inches)*.025

    # 3. Square the answer from step 2
    total_inches = total_inches_CM**2

    # 4. Divide the answer from step 1 by the answer from step 3
    BMI = round(weight_KG / total_inches,1)

    return BMI


def categorizeBMI(bmi):
    """
    Categorize the BMI based off of the user's BMI value
    
        Returns the category name as a string
    """
    if bmi <= 18.6:
        return "underweight"
    elif bmi > 18.6 and bmi <= 24.9:
        return "normal weight"
    elif bmi >= 25 and bmi <= 29.9:
        return "overweight"
    elif bmi >= 30:
        return "obese"


def main():

    print("Welcome to the BMI Index Calculator")
    print("Please enter your height in feet and inches")
    print("    For example if your height is 5'11\", first enter 5 and then enter 11\n")

    measurements = get_user_input()

    feet, inches, pounds = measurements[0],measurements[1],measurements[2]

    BMI = calculateBMI(feet,inches,pounds)
    print(f"Your body mass index (BMI) value is: {BMI}")

    category = categorizeBMI(BMI)
    print(f"You are {category}!")


if __name__ == "__main__":
    main()
