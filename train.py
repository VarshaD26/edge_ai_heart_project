import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
import joblib

# Load data
df = pd.read_csv("heart.csv")

X = df[["age", "trestbps", "chol", "thalach"]]
y = df["target"]

# Save scaler
mean = X.mean()
std = X.std()
X = (X - mean) / std
joblib.dump((mean, std), "scaler.pkl")

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# ✅ FIXED MODEL (IMPORTANT)
model = tf.keras.Sequential([
    tf.keras.Input(shape=(4,)),   # 🔥 THIS FIXES YOUR ERROR
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=20, verbose=1)

# Save model (safe format)
model.save("model.keras")

print("✅ Model retrained correctly!")

# Convert to TFLite (Edge AI friendly)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open("model.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ TFLite model saved!")