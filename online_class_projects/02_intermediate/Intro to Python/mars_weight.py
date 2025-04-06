print("Welcome to the Planet Weight Calculator!")
print("="*40)

# Dictionary of planets and their gravity factors relative to Earth
planet_gravity = {
    "mercury": 0.376,
    "venus": 0.889,
    "mars": 0.378,
    "jupiter": 2.36,
    "saturn": 1.081,
    "uranus": 0.815,
    "neptune": 1.14,
    "earth": 1.0
}

# Get user's choice of planet
planet = input("Enter the planet you want to check your weight on (e.g., Mercury, Venus, Mars, etc.): ").lower()

# Check if the input is a valid planet, otherwise default to Earth
if planet not in planet_gravity:
    print(f"Invalid planet input, defaulting to Earth.")
    planet = "earth"

# Get user's weight on Earth
while True:
    try:
        earth_weight = float(input("Please enter your weight on Earth (kg): "))
        if earth_weight <= 0:
            print("Weight must be a positive number. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

# Calculate the weight on the selected planet
gravity_factor = planet_gravity[planet]
planet_weight = earth_weight * gravity_factor

# Print the result
print(f"\nYour weight on {planet.capitalize()} is: {round(planet_weight, 2)} kg")
