class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        fahrenheit = (celsius * 1.8) + 32
        kelvin = celsius + 273.15
        return [kelvin, fahrenheit]
