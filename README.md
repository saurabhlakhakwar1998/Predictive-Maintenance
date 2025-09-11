# 🏭 Predictive Maintenance - Machine Failure Prediction

This project predicts **machine failures** using sensor data such as temperature, pressure, vibration, torque, and tool wear.  
The goal is to help manufacturing units perform **maintenance before breakdown**, saving cost and downtime.

---

## 📌 Project Structure

```
predictive-maintenance/
├── data/
│   └── sample.csv
├── notebooks/
│   ├── 01_EDA.py
│   └── 02_Modeling.py
├── src/
│   ├── data_loader.py
│   └── inference.py
├── dashboards/
├── models/
├── requirements.txt
└── README.md
```

---

## 🚀 Features
- Loads and analyzes machine sensor data  
- Performs **EDA** (Exploratory Data Analysis) with heatmaps, boxplots, distributions  
- Trains a **Logistic Regression** model to predict failures  
- Saves the trained model for future inference  
- Ready for **Power BI Dashboard** integration

---

## ⚙️ Installation

Clone the repository:
```bash
git clone https://github.com/your-username/predictive-maintenance.git
cd predictive-maintenance
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run EDA:
```bash
python notebooks/01_EDA.py
```

Train Model:
```bash
python notebooks/02_Modeling.py
```

---

## 📊 Example Output

**Correlation Heatmap**  
![Heatmap](https://via.placeholder.com/600x300.png?text=Heatmap+Example)

**Confusion Matrix**  
![Confusion Matrix](https://via.placeholder.com/600x300.png?text=Confusion+Matrix+Example)

---

## 📌 Next Steps
- Improve model using Random Forest / XGBoost  
- Create Power BI dashboard for real-time monitoring  
- Deploy model as REST API for production use  

---

## 👨‍💻 Author
**Saurabh Lakhakwar**  
- 📍 Hinganghat  
- 💼 Aspiring Data Analyst  
- 🔗 [LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com)

---
