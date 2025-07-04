import streamlit as st
import joblib as jb
import numpy as np
energy = jb.load(r"C:\Users\rani ghangare\OneDrive\Documents\Desktop\Python Skill4Future Session\appliance_energy_predictor.pkl")
st.title("Welcome to energy consumption predictor model")
#Input
temp = st.number_input("Temperature (In degree celcius)",
                      min_value = 0.0, max_value = 45.0, value = 5.0)

if st.button("Predict Energy Consumption"):
    new_input = np.array([[temp]])
    prediction = energy.predict(new_input)
    st.write(f"The predicted energy consumption for {temp} degree temperature is {prediction[0]:.2f} Kwh")
    st.write(f"Thank you.....!")
