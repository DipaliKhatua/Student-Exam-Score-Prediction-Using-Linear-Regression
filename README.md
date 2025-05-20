# 📚 Predicting Student Exam Scores Based on Study Hours (Linear Regression)

## 🚀 Project Overview  
This project builds a **Linear Regression model** to predict **student exam scores** based on their **study hours**. The model identifies how study time affects academic performance and provides useful insights for students and EdTech applications.  

## 📂 Directory Structure  
- Artifacts/  (Stores the trained model)
- app.py  (Flask API)
- requirements.txt  (Dependencies)
- README.md  (Project Documentation)

## 🔧 Tech Stack Used  
- **Machine Learning:** Scikit-learn (Linear Regression)  
- **Data Handling:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn  
- **Model Deployment:** Flask  
- **API Testing:** Thunder Client  

## 🏗️ Steps to Set Up & Run  
### **1. Install Dependencies**  
```bash
pip install -r requirements.txt
### 2. Train & Save Model

import pickle

with open("artifacts/linear_regression_model.pkl", "wb") as file:
    pickle.dump(trained_model, file)

### 3. Run the Flask API
python app.py

### 4. Test API with Thunder Client
Send a POST request to:
http://127.0.0.1:5000/predict
With JSON body:
{
  "Hours": 6.5
}

5. Example Response
{
  "Predicted Exam Score": 78.5
}

📊 Model Performance
Evaluation Metric: Mean Absolute Error (MAE)
MAE = 3.37 (Low error, good predictions)


Awesome! Here’s your README.md for the Linear Regression-based Study Hours Prediction project—structured just like the previous one. 🚀

# 📚 Predicting Student Exam Scores Based on Study Hours (Linear Regression)

## 🚀 Project Overview  
This project builds a **Linear Regression model** to predict **student exam scores** based on their **study hours**. The model identifies how study time affects academic performance and provides useful insights for students and EdTech applications.  

## 📂 Directory Structure  


- artifacts/  (Stores the trained model)
- app.py  (Flask API)
- requirements.txt  (Dependencies)
- README.md  (Project Documentation)

## 🔧 Tech Stack Used  
- **Machine Learning:** Scikit-learn (Linear Regression)  
- **Data Handling:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn  
- **Model Deployment:** Flask  
- **API Testing:** Thunder Client  

## 🏗️ Steps to Set Up & Run  
### **1. Install Dependencies**  
```bash
pip install -r requirements.txt


2. Train & Save Model
import pickle
with open("artifacts/linear_regression_model.pkl", "wb") as file:
    pickle.dump(trained_model, file)


3. Run the Flask API
python app.py


Your API will be live at http://127.0.0.1:5000/.
4. Test API with Thunder Client
Send a POST request to:
http://127.0.0.1:5000/predict


With JSON body:
{
  "Hours": 6.5
}


5. Example Response
{
  "Predicted Exam Score": 78.5
}


📊 Model Performance
Evaluation Metric: Mean Absolute Error (MAE)
MAE = 3.37 (Low error, good predictions)


Visualization of Predictions vs Actual Scores
plt.scatter(y_test, y_pred, alpha=0.6, color='blue', label="Predicted")
plt.scatter(y_test, y_test, alpha=0.6, color='red', label="Actual")
plt.xlabel("Actual Exam Scores")
plt.ylabel("Predicted Exam Scores")
plt.title("Linear Regression Predictions vs Actual Scores")
plt.legend()
plt.show()


✨ Author
Dipali Khatua
- Aspiring Data Scientist
- connect me - Dipali Khatua (LinkedIn)









