import streamlit as st

# Dictionary of conversion factors
conversions = {
    "Length": {
        "Meter": 1.0,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701,
    },
    "Weight": {
        "Kilogram": 1.0,
        "Gram": 1000,
        "Milligram": 1e6,
        "Pound": 2.20462,
        "Ounce": 35.274,
    },
    "Temperature": {
        "Celsius": 1.0,
        "Fahrenheit": lambda c: (c * 9/5) + 32,
        "Kelvin": lambda c: c + 273.15
    }
}

# Set page configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Custom Dark Theme Styling
st.markdown(
    """
    <style>
        body { background-color:rgba(255, 183, 183, 0.67); }
        .stApp { background-color:rgba(255, 255, 255, 0.92); padding: 20px; border-radius: 10px; }
        .stMarkdown, .stTextInput, .stSelectbox, .stNumberInput { 
            color: white bold !important;
        }
        .stButton>button {
            background-color:rgba(255, 102, 0, 0.14);
            color: black;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
            border: 1px solidrgba(255, 102, 0, 0.61);
            cursor: pointer;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color:rgb(184, 149, 125);
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Title
st.title(" Smart Unit Converter  🔢📏")
st.subheader("Precision In Every Conversion | Ease In Every Step 🔹✨")

# Select Category
category = st.selectbox("Select Category 🔍", list(conversions.keys()))

# Select Units
unit_options = list(conversions[category].keys())
from_unit = st.selectbox("Convert from 🔄", unit_options)
to_unit = st.selectbox("Convert to  🔁", unit_options)

# Input Value
value = st.number_input("Enter value ⏳ ", min_value=0.0, format="%.2f")

# Convert Button
if st.button("Convert"):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = conversions["Temperature"]["Fahrenheit"](value)
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = conversions["Temperature"]["Kelvin"](value)
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = ((value - 32) * 5/9) + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = ((value - 273.15) * 9/5) + 32
        else:
            result = value
    else:
        result = value * (conversions[category][to_unit] / conversions[category][from_unit])

    # Display Result
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")



#footer
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left:0;
            width: 100%;
            background-color: #222831;
            color: #ffffff;
            text-align: center;
            padding: 10px;
            font-weight: bold;
            font-size: 16px;
        }
    </style>
    <div class="footer">
        Developed With ❤️ By <b>Rahima Shaikh Using Streamlit</b>
    </div>
    """,
    unsafe_allow_html=True
)
