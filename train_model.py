import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("dataset/instagram_fake_accounts.csv")

# Features and target
X = data.drop("fake", axis=1)
y = data["fake"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
print("Model Accuracy:", accuracy_score(y_test, predictions))

# User input prediction
followers = int(input("Enter number of followers: "))