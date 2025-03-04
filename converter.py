
import streamlit as st  # type: ignore
st.markdown(
    """
<style>
body {
    background-color: #f0f2f6;
    color: white;
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 0;
}
.stApp {
    display: flex;
    flex-direction: row;
}
.sidebar {
    width: 250px;
    height: 100vh;
    background: linear-gradient(135deg, #0b5394, #351c75);
    padding: 20px;
    box-shadow: 3px 0 15px rgba(0, 0, 0, 0.3);
    position: fixed;
    left: 0;
    top: 0;
    transition: all 0.3s ease-in-out;
}
.sidebar:hover {
    width: 270px;
}
.main-content {
    margin-left: 270px;
    padding: 30px;
    width: calc(100% - 270px);
}
h1 {
    text-align: center;
    font-size: 36px;
    color: #222;
    animation: fadeIn 1.2s ease-in-out;
}
.stButton>button {
    background: linear-gradient(45deg, #0b5394, #351c75);
    color: white;
    padding: 12px 25px;
    border: none;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0, 201, 255, 0.4);
    transition: all 0.3s;
    font-size: 16px;
    cursor: pointer;
}
.stButton>button:hover {
    background: linear-gradient(45deg, #92fe9d, #00c9ff);
    transform: scale(1.05);
    color: black;
}
.result-box {
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
    box-shadow: 0 5px 15px rgba(0, 201, 255, 0.3);
    animation: slideUp 0.5s ease-in-out;
}
.footer {
    text-align: center;
    margin-top: 50px;
    font-size: 14px;
    color: black;
}
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

</style>
""",
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1> Unit Converter  </h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Milimeters", "Yards", "Kilometers", "Feet", "Miles", "Inches"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Milimeters", "Yards", "Kilometers", "Feet", "Miles", "Inches"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Miligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Miligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion logic
def length_convertor(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Milimeters": 1000,
        "Yards": 1.09361,
        "Feet": 3.28,
        "Miles": 0.000621371,
        "Inches": 39.37,
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,  
        "Grams": 1000,  
        "Miligrams": 1000000,  
        "Pounds": 2.20462,  # ✅ Sahi value
        "Ounces": 35.274,   # ✅ Sahi value
    }
    value_in_kg = value / weight_units[from_unit]
    result = value_in_kg * weight_units[to_unit]

    return round(result, 4) 








def temp_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

if st.button("Convert"):
    result = None  # Default value

    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_convertor(value, from_unit, to_unit)

    # Result ko check karo, agar None nahi hai tabhi show karo
    if result is not None:
        st.markdown(f"<div class='result-box'> {value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

    # Footer show karne ke liye
    st.markdown("<div class='footer'> Created By Programming with Abdullah</div>", unsafe_allow_html=True)
