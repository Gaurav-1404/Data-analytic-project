# 🚔 AI-Based Crime Analysis & Prediction System

## 📌 Project Overview

This project focuses on analyzing crime cases against police personnel using **Data Analytics and Machine Learning**. It helps identify trends, high-risk regions, and provides predictive insights to support better decision-making.

The system uses real-world data (2016–2018) and presents insights through an **interactive dashboard**.

---

## 🎯 Objectives

* Analyze crime cases across different states
* Identify trends over time
* Detect high-risk areas with maximum cases
* Compare arrest vs conviction rates
* Predict probability of conviction using ML

---

## 📊 Dataset

* Source: NCRB / Kaggle datasets
* Data includes:

  * State/UT
  * Number of cases registered
  * Police personnel arrested
  * Chargesheeted cases
  * Convictions & acquittals
  * Year (2016–2018)

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, Matplotlib
* **Machine Learning:** Scikit-learn
* **Dashboard:** Streamlit

---

## 📁 Project Structure

```
crime-analytics/
│
├── data/
│   └── crime_data.csv
│
├── src/
│   ├── preprocessing.py
│   ├── analysis.py
│   └── model.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Features

* 📊 State-wise crime analysis
* 📈 Year-wise trend visualization
* 🔥 Top 5 high-crime states detection
* 🤖 Machine Learning model for prediction
* 🖥️ Interactive Streamlit dashboard

---

## 🧹 Data Preprocessing

* Merged multiple datasets (2016–2018)
* Handled missing values
* Removed unnecessary columns
* Feature engineering (Year, rates)

---

## 📈 Analysis Performed

* Crime distribution across states
* Trend analysis over years
* Conviction vs arrest comparison
* Identification of high-risk regions

---

## 🤖 Machine Learning

* Model: Random Forest Classifier
* Objective: Predict whether a case leads to conviction
* Features used:

  * Number of cases registered
  * Number of personnel arrested

---

## 📊 Key Insights

* Some states show **high crime but low conviction rates**
* Significant gap between **arrests and convictions**
* Trend analysis helps identify **patterns over time**
* Indicates possible **inefficiencies in the justice system**

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/crime-analytics.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
streamlit run app.py
```

---

## 🖥️ Output

* Interactive dashboard
* Graphs and visualizations
* Machine learning prediction results

---

## 🚀 Future Scope

* Add real-time crime data
* Implement advanced ML models (XGBoost, LSTM)
* Integrate Power BI dashboards
* Add geospatial heatmaps (India map)
* Deploy on cloud (Streamlit Cloud / AWS)

---

## 🧾 Resume Description

Developed an AI-based Crime Analysis & Prediction System using Python, Pandas, and Scikit-learn. Built interactive dashboards with Streamlit to visualize trends and identify high-risk regions. Implemented a machine learning model to predict conviction outcomes based on historical data.

---

## 👨‍💻 Author

**Gaurav Gupta**

---

## ⭐ Acknowledgment

Dataset sourced from NCRB / Kaggle.
This project is developed for academic and learning purposes.

---
