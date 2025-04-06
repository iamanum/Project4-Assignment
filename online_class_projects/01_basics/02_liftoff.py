import time

# Take the starting number for the countdown
number = int(input("Enter the number where you want to start counting: "))

# Countdown loop
for i in range(number, 0, -1):
    time.sleep(1)  # Delay of 1 second between each number
    print(i)

# Final message
print("Liftoff!!! 🚀")
