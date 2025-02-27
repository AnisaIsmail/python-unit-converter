import streamlit as st
from math import pi

# Function for length conversion
def length_converter(value, from_unit, to_unit):
    units = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34,
        'yards': 0.9144,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'foots': 3.28084,
        'micrometers': 1e+6,
        'nanometers': 1e+9,
        'inch': 39.3701,
        'nautical miles': 0.000539957
    }
    return value * (units[to_unit] / units[from_unit])

# Function for weight conversion
def weight_converter(value, from_unit, to_unit):
    units = {
        'grams': 1,
        'kilograms': 1000,
        'pounds': 453.592,
        'ounces': 28.3495
    }
    return value * (units[to_unit] / units[from_unit])

# Function for temperature conversion
def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value

# Manually defined currency conversion rates
conversion_rates = {
    'USD': {'INR': 87.17, 'EUR': 0.95, 'GBP': 0.79, 'AUD': 1.59, 'PKR': 280.22, 'SAR': 3.75},
    'INR': {'USD': 0.011, 'EUR': 0.011, 'GBP': 0.0090, 'AUD': 0.018, 'PKR': 3.21, 'SAR': 0.043},
    'EUR': {'USD': 1.05, 'INR': 91.35, 'GBP': 0.83, 'AUD': 1.66, 'PKR': 293.63, 'SAR': 3.93},
    'GBP': {'USD': 1.27, 'INR': 110.51, 'EUR': 1.21, 'AUD': 2.01, 'PKR': 354.80, 'SAR': 4.75},
    'AUD': {'USD': 0.63, 'INR': 54.91, 'EUR': 0.60, 'GBP': 0.50, 'PKR': 171.61, 'SAR': 2.36},
    'PKR': {'USD': 0.0036, 'INR': 0.31, 'EUR': 0.0034, 'GBP': 0.0028, 'AUD': 0.0057, 'SAR': 0.013},
    'SAR': {'USD': 0.27, 'INR': 23.24, 'EUR': 0.25, 'GBP':0.21, 'AUD': 0.42, 'PKR': 74.56}
}

# Function for currency conversion with manual rates
def currency_converter(amount, from_currency, to_currency):
    try:
        if from_currency == to_currency:
            return amount
        if from_currency in conversion_rates and to_currency in conversion_rates[from_currency]:
            conversion_rate = conversion_rates[from_currency][to_currency]
            result = amount * conversion_rate
            return result
        else:
            raise Exception(f"Conversion rate from {from_currency} to {to_currency} not available.")
    except Exception as e:
        st.error(f"Currency conversion failed: {e}")
        return None

# Function for volume conversion
def volume_converter(value, from_unit, to_unit):
    units = {
        'liters': 1,
        'milliliters': 0.001,
        'gallons': 3.78541,
        'cubic meters': 1000,
        'cubic centimeters': 0.001
    }
    return value * (units[to_unit] / units[from_unit])

# Function for height conversion
def height_converter(value, from_unit, to_unit):
    units = {
        'meters': 1,
        'centimeters': 100,
        'feet': 3.28084,
        'inches': 39.3701
    }
    return value * (units[to_unit] / units[from_unit])

# Function to calculate area of circle (example of custom unit conversion)
def circle_area(radius):
    return pi * radius * radius

# Streamlit interface
def main():
    st.title("Welcome to Unit Converter! 💰🌍✨")
    st.write("Choose a conversion type from the sidebar ⬅️")
    
    # Sidebar
    st.sidebar.title("Select Conversion Type")
    conversion_type = st.sidebar.radio(
        "Choose conversion type",
        ["Length", "Weight", "Temperature", "Currency", "Volume", "Height", "Circle Area"]
    )
    
    # Checkbox for "How to Use"
    show_how_to_use = st.sidebar.checkbox('How to use?')
    if show_how_to_use:
        st.sidebar.write(""" 
        ### How to Use:
        1. Select the conversion type (e.g., Length, Weight, Temperature).
        2. Enter the value you want to convert.
        3. Select the units you want to convert from and to.
        4. Press "Convert" to see the result.
        """)
    
    # Length Conversion
    if conversion_type == "Length":
        value = st.number_input("Enter value", min_value=0.0)
        from_unit = st.selectbox("From unit", ["meters", "kilometers", "miles", "yards", "centimeters", "millimeters", "foots", "micrometres","nanometers", "inch", "nautical miles"])
        to_unit = st.selectbox("To unit", ["meters", "kilometers", "miles", "yards", "centimeters", "millimeters", "foots", "micrometres","nanometers", "inch", "nautical miles"])
        if st.button("Convert 💡"):
            result = length_converter(value, from_unit, to_unit)
            st.write(f"{value} {from_unit} = {result} {to_unit}")
            st.snow()

    # Weight Conversion
    elif conversion_type == "Weight":
        value = st.number_input("Enter value", min_value=0.0)
        from_unit = st.selectbox("From unit", ["grams", "kilograms", "pounds", "ounces"])
        to_unit = st.selectbox("To unit", ["grams", "kilograms", "pounds", "ounces"])
        if st.button("Convert 💡"):
            result = weight_converter(value, from_unit, to_unit)
            st.write(f"{value} {from_unit} = {result} {to_unit}")
            st.snow()

    # Temperature Conversion
    elif conversion_type == "Temperature":
        value = st.number_input("Enter value", min_value=-273.15)
        from_unit = st.selectbox("From unit", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("To unit", ["Celsius", "Fahrenheit", "Kelvin"])
        if st.button("Convert 💡"):
            result = temperature_converter(value, from_unit, to_unit)
            st.write(f"{value}° {from_unit} = {result}° {to_unit}")
            st.snow()

    # Currency Conversion
    elif conversion_type == "Currency":
        amount = st.number_input("Enter amount", min_value=0.0)
        from_currency = st.selectbox("From currency", ["USD", "INR", "EUR", "GBP", "AUD", "PKR", "SAR"])
        to_currency = st.selectbox("To currency", ["USD", "INR", "EUR", "GBP", "AUD", "PKR", "SAR"])
        if st.button("Convert 💡"):
            result = currency_converter(amount, from_currency, to_currency)
            if result:
                st.write(f"{amount} {from_currency} = {result} {to_currency}")
                st.snow()
                
    # Volume Conversion
    elif conversion_type == "Volume":
        value = st.number_input("Enter value", min_value=0.0)
        from_unit = st.selectbox("From unit", ["liters", "milliliters", "gallons", "cubic meters", "cubic centimeters"])
        to_unit = st.selectbox("To unit", ["liters", "milliliters", "gallons", "cubic meters", "cubic centimeters"])
        if st.button("Convert 💡"):
            result = volume_converter(value, from_unit, to_unit)
            st.write(f"{value} {from_unit} = {result} {to_unit}")
            st.snow()

    # Height Conversion
    elif conversion_type == "Height":
        value = st.number_input("Enter value", min_value=0.0)
        from_unit = st.selectbox("From unit", ["meters", "centimeters", "feet", "inches"])
        to_unit = st.selectbox("To unit", ["meters", "centimeters", "feet", "inches"])
        if st.button("Convert 💡"):
            result = height_converter(value, from_unit, to_unit)
            st.write(f"{value} {from_unit} = {result} {to_unit}")
            st.snow()

    # Circle Area Calculation
    elif conversion_type == "Circle Area":
        radius = st.number_input("Enter radius of circle", min_value=0.0)
        if st.button("Calculate Area 💡"):
            result = circle_area(radius)
            st.write(f"Area of circle with radius {radius} is {result} square units")
            st.snow()
            

if __name__ == "__main__":
    main()