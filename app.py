import streamlit as st
from utils.prediction_utils import predict_pneumonia
from utils.ocr_utils import extract_text_from_pdf, extract_text_from_image
from utils.chat_with_report import chat_with_report
from utils.summarizer import summarize_report

# Page configuration
st.set_page_config(page_title="Disease Diagnosis & Report Summarizer", layout="wide")

st.title("🩺 Disease Diagnosis & Medical Report Summarizer")

# Sidebar for navigation
option = st.sidebar.selectbox(
    "Select Diagnosis Module",
    ["Brain Tumor Detection", "Pneumonia Detection", "Diabetes Prediction", "Heart Disease Prediction"]
)

st.sidebar.markdown("---")
uploaded_report = st.sidebar.file_uploader("Upload Medical Report (PDF/Image/Text)", type=['pdf', 'png', 'jpg', 'jpeg', 'txt'])

if uploaded_report:
    st.sidebar.success("Report uploaded successfully!")

    # Extract text based on file type
    if uploaded_report.type == "application/pdf":
        report_text = extract_text_from_pdf(uploaded_report)
        st.write("PDF extraction not implemented yet.")
    elif uploaded_report.type.startswith("image"):
        report_text = extract_text_from_image(uploaded_report)
        st.write("Image extraction not implemented yet.")
    else:
        report_text = uploaded_report.read().decode("utf-8")

    st.subheader("📑 Uploaded Report Text")
    st.write(report_text)

    # LLM Summarization
    summary = summarize_report(report_text)
    st.subheader("📝 Report Summary")
    st.write(summary)

    st.subheader("💬 Ask questions about the report")
    user_input = st.text_input("Your question")

    if user_input and report_text:
        response = chat_with_report(report_text, user_input)
    st.markdown(f"**Assistant:** {response}")

# Module based UI
if option == "Brain Tumor Detection":
    uploaded_image = st.file_uploader("Upload MRI Image", type=["png", "jpg", "jpeg"])
    if uploaded_image:
        # prediction = predict_brain_tumor(uploaded_image)
        st.success(f"Prediction: {1}")

elif option == "Pneumonia Detection":
    uploaded_image = st.file_uploader("Upload Chest X-Ray", type=["png", "jpg", "jpeg"])
    if uploaded_image:
        prediction = predict_pneumonia(uploaded_image)
        st.success(f"Prediction: {prediction}")

elif option == "Diabetes Prediction":
    glucose = st.number_input("Glucose Level")
    bmi = st.number_input("BMI")
    age = st.number_input("Age")
    if st.button("Predict Diabetes"):
        # prediction = predict_diabetes(glucose, bmi, age)
        st.success(f"Prediction: {3}")

elif option == "Heart Disease Prediction":
    age = st.number_input("Age")
    cholesterol = st.number_input("Cholesterol")
    bp = st.number_input("Blood Pressure")
    if st.button("Predict Heart Disease"):
        # prediction = predict_heart_disease(age, cholesterol, bp)
        st.success(f"Prediction: {4}")
