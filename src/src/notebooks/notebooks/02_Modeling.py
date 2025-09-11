# 02_Modeling.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/sample.csv")
print("✅ Data Loaded for Modeling")

# Drop non-numeric columns (like machine_id)
X = df.select_dtypes(include=['float64', 'int64']).drop(columns=["failure"])
y = df["failure"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(f"📊 Training Samples: {X_train.shape[0]}, Test Samples: {X_test.shape[0]}")

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)
print("✅ Model Training Completed")

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("\n📈 Classification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Save the model
joblib.dump(model, "models/model.pkl")
print("💾 Model saved to models/model.pkl")
