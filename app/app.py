import pickle
import streamlit as st

# deserializing pickle file
def loading_model():
    try:
        with open("../notebooks/final_model.pickle","br") as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError as e:
        st.write(e)
        

def main():
    try:
        st.title("Diabeties Classify")
        col1, col2 = st.columns(2)
        with col1:
            pregnancies = st.text_input("Number of times pregnant")
        with col2:
            glucose = st.text_input("Glucose Level")

        col3, col4, col5 = st.columns(3)
        with col3:
            blood_pressure = st.text_input("Diastolic blood pressure (mm Hg)")
        with col4:
            skin_thickness = st.text_input("Triceps skin fold thickness (mm)")
        with col5:
            insulin = st.text_input("serum insulin (mu U/ml)")
        col6, col7, col8 = st.columns(3)
        with col6:
            bmi = st.text_input("Body mass index")
        with col7:
            diabetes_pedigree_function = st.text_input("Diabetes Pedigree Function")
        with col8:
            age = st.text_input("Age (years)")

        
    except ValueError as e:
        st.write(e)
if __name__ == "__main__":
    main()
