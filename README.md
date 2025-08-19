# Heart Disease Prediction Project

## Description
This project predicts heart disease risk using machine learning. It includes:
- Data preprocessing & cleaning
- Dimensionality reduction (PCA)
- Feature selection
- Supervised learning: Logistic Regression, Decision Tree, Random Forest, SVM
- Unsupervised learning: K-Means, Hierarchical Clustering
- Hyperparameter tuning
- Streamlit UI for real-time predictions
- Model and evaluation metrics saved

## Folder Structure
Heart_Disease_Project/
│── data/

│ ├── heart_disease.csv

│── notebooks/

│ ├── 01_data_preprocessing.ipynb
│ ├── 02_pca_analysis.ipynb
│ ├── 03_feature_selection.ipynb
│ ├── 04_supervised_learning.ipynb
│ ├── 05_unsupervised_learning.ipynb
│ ├── 06_hyperparameter_tuning.ipynb

│── models/
│ ├── final_model.pkl

│── ui/
│ ├── app.py (Streamlit UI)

│── deployment/
│ ├── ngrok_setup.txt

│── results/
│ ├── evaluation_metrics.txt

│── README.md

│── requirements.txt

│── .gitignore


---

## 📌 Features

- **Data Preprocessing & Cleaning**
  - Handle missing values
  - Encode categorical variables
  - Standardize numerical features
  - Exploratory Data Analysis (EDA)
  
- **Dimensionality Reduction**
  - Principal Component Analysis (PCA)
  - Variance analysis and visualization

- **Feature Selection**
  - Random Forest / XGBoost feature importance
  - Recursive Feature Elimination (RFE)
  - Chi-Square test

- **Supervised Learning Models**
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Support Vector Machine (SVM)
  - Model evaluation (Accuracy, Precision, Recall, F1-score, ROC-AUC)

- **Unsupervised Learning**
  - K-Means Clustering
  - Hierarchical Clustering
  - Comparison with actual labels

- **Hyperparameter Tuning**
  - GridSearchCV & RandomizedSearchCV
  - Optimized model selection

- **Model Deployment**
  - Model exported as `.pkl`
  - Streamlit web interface for real-time predictions
  - Ngrok for public access (optional)

---

## 📊 Evaluation Metrics

| Model                 | Accuracy | Precision | Recall  | F1      | ROC_AUC |
|----------------------|---------|-----------|---------|---------|---------|
| Logistic Regression   | 0.867   | 0.864     | 0.792   | 0.826   | 0.948   |
| Random Forest         | 0.800   | 0.773     | 0.708   | 0.739   | 0.888   |
| Gradient Boosting     | 0.783   | 0.739     | 0.708   | 0.723   | 0.896   |
| SVM                   | 0.867   | 0.900     | 0.750   | 0.818   | 0.964   |




