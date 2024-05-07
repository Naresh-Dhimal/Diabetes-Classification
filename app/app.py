import pickle
import streamlit as st

# deserializing pickle file
def loading_model():
    try:
        with open("app/final_model.pickle","br") as file:
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
            blood_pressure = st.text_input("BloodPressure")
        with col4:
            skin_thickness = st.text_input("SkinThickness")
        with col5:
            insulin = st.text_input("Insulin")
        col6, col7, col8 = st.columns(3)
        with col6:
            bmi = st.text_input("Body mass index")
        with col7:
            diabetes_pedigree_function = st.text_input("Diabetes Pedigree Function")
        with col8:
            age = st.text_input("Age (years)")

       
        col100, col200, c0l300 = st.columns(3)
        if col200.button("Classify"):
            pass
            model = loading_model()
            classified = model.predict([[float(pregnancies), float(glucose), float(blood_pressure), float(skin_thickness), float(insulin), float(bmi), float(diabetes_pedigree_function), float(age)]])
            if classified[0] == 1:
                st.write("The patient is predicted to have diabetes.")
            else:
                st.write("The patient is predicted to not have diabetes.")
    except ValueError as e:
        st.write(e)
if __name__ == "__main__":
    main()
