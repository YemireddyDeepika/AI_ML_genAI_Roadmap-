import os

folders = [
    "Day01_NumPy_Basics",
    "Day02_NumPy_Advanced",
    "Day03_Pandas_Basics",
    "Day04_Data_Cleaning",

    "Machine_Learning_Projects/Student_Performance_Prediction",
    "Machine_Learning_Projects/Loan_Approval_System",
    "Machine_Learning_Projects/Customer_Segmentation",

    "Deep_Learning_Projects/Digit_Recognition_MNIST",
    "Deep_Learning_Projects/Face_Recognition_System",
    "Deep_Learning_Projects/Sentiment_Analysis",

    "Generative_AI_Projects/AI_Chatbot",
    "Generative_AI_Projects/PDF_QA_RAG_System",
    "Generative_AI_Projects/Resume_Analyzer"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("✅ Repository structure created successfully!")
