import streamlit as st
import pandas as pd

@st.cache
def load_data():
    df = pd.read_csv("FYP good data_tensile_today.csv")
    return df

df = load_data()

def show_explore_page():
    st.title("Explore compound parameters vs mixer settings")

    st.write(
        """
    ### Compound B09255
    """
    )

    st.write(
        """
    #### Tensile vs Step 7 Energy
    """
    )

    data = df.groupby(["Tensile"])["Step7-Energy-rel-kWh"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Tensile vs Step 7 Temperature
    """
    )

    data = df.groupby(["Tensile"])["Step7-Temperature-C-F"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Tensile vs Step 7 Torque
    """
    )

    data = df.groupby(["Tensile"])["Step7-Torque-Nm-ft/lbs"].mean().sort_values(ascending=True)
    st.bar_chart(data)