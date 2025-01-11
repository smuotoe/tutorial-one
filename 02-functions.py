# Functions and Lambda Expressions Practice Exercise

# 1. Create a function that takes a list of temperatures in Celsius
# and returns a dictionary with the average, minimum, and maximum temperatures
def analyze_temperatures(temperatures: list[float]) -> dict:
    # TODO: Implement this function
    pass


# 2. Create a lambda function that converts Celsius to Fahrenheit
# Formula: (C × 9/5) + 32
celsius_to_fahrenheit = None  # TODO: Replace with lambda function

if __name__ == "__main__":
    # Example usage
    sample_temps = [23.5, 25.1, 24.3, 25.8, 23.9]

    # Print analysis of sample temperatures
    print("\nAnalyzing temperatures:", sample_temps)
    stats = analyze_temperatures(sample_temps)
    for key, value in stats.items():
        print(f"{key}: {value}")
