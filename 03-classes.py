# Classes and Object-Oriented Programming Exercise

class WeatherStation:
    """
    A class representing a weather station that can track temperature readings
    and provide various statistics and conversions.
    """

    def __init__(self, location: str):
        """
        Initialize a WeatherStation with a location name.
        Set up any required instance variables here.

        Parameters:
            location (str): The location of the weather station
        """
        # TODO: Initialize instance variables
        pass

    def add_temperature(self, celsius_temp: float) -> bool:
        """
        Add a temperature reading in Celsius.
        Should validate that the temperature is between -50°C and 50°C.

        Parameters:
            celsius_temp (float): Temperature reading in Celsius

        Returns:
            bool: True if temperature was added successfully, False if invalid
        """
        # TODO: Implement this method
        pass

    def get_stats(self) -> dict:
        """
        Calculate statistics for all recorded temperatures.

        Returns:
            dict: Dictionary containing:
                - average: average temperature
                - min: minimum temperature
                - max: maximum temperature
                - range: difference between max and min
                - count: number of readings
        """
        # TODO: Implement this method
        pass

    def get_fahrenheit_readings(self) -> list[float]:
        """
        Convert all stored temperature readings to Fahrenheit.

        Returns:
            list[float]: List of temperatures in Fahrenheit
        """
        # TODO: Implement this method
        pass

    def clear_readings(self) -> None:
        """
        Clear all stored temperature readings.
        """
        # TODO: Implement this method
        pass


if __name__ == "__main__":
    # Example usage
    station = WeatherStation("San Francisco")

    # Add some temperature readings
    temperatures = [15.5, 17.2, 19.0, 16.8, 15.9]
    for temp in temperatures:
        station.add_temperature(temp)

    # Get and print statistics
    stats = station.get_stats()
    print("\nTemperature Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")

    # Print Fahrenheit conversions
    print("\nTemperatures in Fahrenheit:")
    for temp in station.get_fahrenheit_readings():
        print(f"{temp:.1f}°F")
