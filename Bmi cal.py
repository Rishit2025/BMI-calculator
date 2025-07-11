def calculate_bmi(weight, height):
    """Calculate BMI using the formula: weight (kg) / height^2 (m^2)"""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify the BMI into standard health categories"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_valid_input(prompt):
    """Get valid float input from the user"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("=== BMI Calculator ===")
    
    # Get user inputs with validation
    weight = get_valid_input("Enter your weight in kilograms (kg): ")
    height = get_valid_input("Enter your height in meters (m): ")

    # Calculate and classify BMI
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    # Display result
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
