import streamlit as st
import pandas as pd
import pickle

# 1. Load the trained model we saved earlier
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

# 2. Design the Web App Interface UI
st.title("🎓 Student Performance Predictor")
st.write("Adjust the sliders below to predict a student's final exam score using our trained AI model.")

st.header("📊 Student Inputs")

# Interactive Sliders for Input
hours_studied = st.slider("Hours Studied (Per Week)", min_value=1.0, max_value=10.0, value=7.0, step=0.5)
attendance = st.slider("Attendance Percentage (%)", min_value=0, max_value=100, value=85, step=1)
sleep_hours = st.slider("Sleep Hours (Per Night)", min_value=4.0, max_value=10.0, value=7.0, step=0.5)

# 3. Handle Prediction Action
if st.button("🔮 Predict Exam Score"):
    # Structure the inputs exactly like our model expects
    input_data = pd.DataFrame(
        [[hours_studied, attendance, sleep_hours]], 
        columns=['Hours_Studied', 'Attendance_Pct', 'Sleep_Hours']
    )
    
    # Run the prediction
    prediction = model.predict(input_data)[0]
    
    # Clip results to realistic ranges (0% to 100%)
    final_score = max(0, min(100, prediction))
    
    # Display the result color-coded
    if final_score >= 75:
        st.success(f"### Predicted Exam Score: **{round(final_score, 2)}%** 🌟")
    elif final_score >= 50:
        st.info(f"### Predicted Exam Score: **{round(final_score, 2)}%** 👍")
    else:
        st.error(f"### Predicted Exam Score: **{round(final_score, 2)}%** ⚠️")