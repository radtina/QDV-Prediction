import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]

def show_predict_page():
    st.title("QDV Level Check Prediction")

    st.write("""### We need some information to predict the Tensile, Elongation, Hardness & M16,T40 parameters for the B09255 compound. """)

    step_6_energy = st.number_input("Step 6 Energy")
    step_6_temperature = st.number_input("Step 6 Temperature")
    step_6_torque = st.number_input("Step 6 Torque")
    step_7_energy = st.number_input("Step 7 Energy")
    step_7_temperature = st.number_input("Step 7 Temperature")
    step_7_torque = st.number_input("Step 7 Torque")
    step_8_energy = st.number_input("Step 8 Energy")
    step_8_temperature = st.number_input("Step 8 Temperature")
    step_8_torque = st.number_input("Step 8 Torque")

    ok = st.button("Predict Parameters")
    if ok:
        xVar = np.array([[step_6_energy, step_6_temperature, step_6_torque, step_7_energy, step_7_temperature, step_7_torque, step_8_energy, step_8_temperature, step_8_torque,]])
        x = np.all(xVar)
        if x == False:
            st.subheader(f"Please enter all non-zero values.")
        elif x == True:
            answer = regressor.predict(xVar)
            st.subheader(f"Estimated tensile is {round(answer[0][0],5)}")
            st.subheader(f"Estimated elongation is {round(answer[0][1],5)}")
            st.subheader(f"Estimated hardness is {round(answer[0][2],5)}")
            st.subheader(f"Estimated M16,T40 is {round(answer[0][3],5)}")