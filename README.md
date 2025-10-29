# 🏠 California House Price Prediction App

A simple **Streamlit web app** built using the dataset from *Hands-On Machine Learning by Aurélien Géron*.  
It predicts median house prices in California based on location and demographic features.

---

## 🚀 Features
- Interactive sidebar for input parameters  
- Machine learning model trained on the California housing dataset  
- Deployed using **Streamlit Cloud**

---

## 📂 Tech Stack
- Python  
- Scikit-learn  
- Pandas  
- Streamlit  

---

## 🧠 Model
The model was trained following the pipeline in *Hands-On Machine Learning (2nd Edition)*.  
It uses a **RandomForestRegressor** trained on cleaned housing data.

---

## ⚙️ Run Locally
```bash
git clone https://github.com/meghmala-code/california-house-price-predictor.git
cd california-house-price-predictor
pip install -r requirements.txt
streamlit run app.py

