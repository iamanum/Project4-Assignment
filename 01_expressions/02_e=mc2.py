# Constants
ask_question: str = "Enter mass in kilograms: "
speed_of_light: int = 299792458  # Speed of light in m/s

# Prompt user for mass
mass = int(input(ask_question))

# Function to calculate energy using E = m * C^2
def calculate_energy(mass: int) -> int:
    energy = mass * speed_of_light**2
    return energy

# Display the calculated energy
print(f'Energy: {calculate_energy(mass)} joules')
