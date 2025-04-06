
📌 Project Title:
AI-powered-Multi-Disease-Prediction

📝 Project Description:
AI-powered-Multi-Disease-Prediction is an intelligent, interactive, and user-friendly AI-powered health assistant that predicts the likelihood of various diseases based on a user’s medical demographics, lab reports, and imaging data. The system is designed using Streamlit for the frontend, integrated with machine learning models for disease prediction and LLMs (like OpenAI/Gemini) to generate human-understandable diagnostic summaries and health recommendations.

This tool helps patients , any person , medical practitioners to get preliminary health insights and educational content without the need for manual analysis or interpretation of complex medical data.

🚀 Key Features:
🧪 Multi-Disease Prediction Interface
Interactive dashboard for users to choose between different diseases like Heart Disease, Kidney Disease, Liver Disease, etc.

📋 Dynamic Medical Form for Each Disease
Tailored forms appear based on the selected disease, collecting relevant:

Demographics (Age, Gender, Weight, etc.)

Medical test parameters (BP, Glucose, Creatinine, etc.)

Uploaded reports (e.g., CBC, X-rays, MRI scans, PDFs)

🤖 ML-Based Prediction Engine
Each disease has a dedicated trained ML model that processes input features and predicts whether the user has that condition, with risk scoring.

🧠 LLM-Powered Explanation Generator
After prediction, a large language model (LLM) like GPT-4/Gemini creates a detailed, readable explanation of the diagnosis:

Disease overview

Symptoms & risk factors

Possible treatments or next steps

Lifestyle suggestions

📎 File Uploads & Processing Users can upload:

Medical reports (PDFs, CSVs)

X-rays/MRI images (JPEG/PNG)

Reports will be parsed using OCR (Tesseract, PyMuPDF, OpenCV)

📊 Result Dashboard The system provides:

A clear diagnosis

Risk percentage

LLM-generated medical summary

Downloadable report

