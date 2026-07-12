Python Weather Analyzer

# Difficulty : Medium
# Use :  Lambda Function

# Problem

-- Use lambda fun to analyse the weather by the given user_input

## Solution
def weather_analysis(temperature, humidity, wind_speed):
    print("Welcome to the Weather Analysis Tool!")

    to_fahrenheit = lambda c: c * 9 / 5 + 32

    humidity_status = lambda humidity: (
        "High" if humidity > 70 else "Low"
    )

    wind_category = lambda speed: (
        "Strong" if speed > 40
        else "Moderate" if  speed > 20
        else "Low"
    )

    print(f"Temperature in Fahrenheit: {to_fahrenheit(temperature):.2f}°F")
    print(f"Humidity Level: {humidity_status(humidity)}")
    print(f"Wind Speed Category: {wind_category(wind_speed)}")
