# AI Text Detector
# 🧠 AI Text Detector  

## 📌 Overview  
AI Text Detector is a **machine learning-powered web application** designed to classify whether a given text is **AI-generated or human-written**. It uses **TF-IDF vectorization** and a **Support Vector Machine (SVM) classifier** to perform text classification.

---

## 🚀 Features  
✅ **AI vs. Human text detection**  
✅ **Real-time predictions using Streamlit UI**  
✅ **Text preprocessing (punctuation removal, contraction expansion, etc.)**  
✅ **Pretrained ML model (SVM)** for accurate classification  

---

## 🛠️ Tech Stack  
| Technology      | Purpose |
|----------------|---------|
| **Python**     | Core Programming Language |
| **Streamlit**  | UI Framework |
| **Scikit-learn** | ML Model Training & Prediction |
| **Pandas, NumPy** | Data Processing |
| **Pickle** | Model Serialization |

---

## 📂 Project Structure  
📁 AI_Text_Detector
│── 📜 clf.pkl # Pretrained SVM model
│── 📜 tfidf.pkl # TF-IDF vectorizer
│── 📜 zi.py # Main Streamlit application
│── 📜 .gitignore # Ignored files for Git
│── 📜 requirements.txt # Dependencies list
│── 📜 README.md # Project documentation



---

## 🔧 Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Ayman-ilias/Ai_TEXT_DETECTOR.git
cd Ai_TEXT_DETECTOR

### 2️⃣ Set Up Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Run the Application
streamlit run zi.py

## 📝 Usage
1️⃣ Enter text in the provided text area.
2️⃣ Click "Detect" to classify the text.
3️⃣ The model outputs whether the text is AI-generated or human-written.


## 🔍 Model Details
Vectorization: TF-IDF (Term Frequency - Inverse Document Frequency)
Classifier: Support Vector Machine (SVM)
Preprocessing Steps:
Text lowercasing
Punctuation removal
Contraction expansion (e.g., "don't" → "do not")
Whitespace cleanup

## 📌 Example Prediction
Input: "This text was written by an AI and is completely synthetic."
Prediction: "This text appears to be AI-generated."

## 📜 .gitignore File
The .gitignore file ensures that unwanted files are not tracked in the repository. It includes:

*.csv (CSV datasets)
*.pkl (Model files if needed)
venv/ (Virtual environment)


## 🤝 Contributing
Want to improve this project? Feel free to fork the repository, create a feature branch, and submit a pull request!

## 📬 Contact
📌 Developer: Ayman
📌 GitHub Repo: AI Text Detector


## 🚀 Happy Coding! 🎯


