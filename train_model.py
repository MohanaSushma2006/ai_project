import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

# Sample data
X = np.array([
    [7, 6, 2],
    [8, 7, 3],
    [6, 5, 1],
    [9, 8, 4]
])

y = np.array([0, 1, 0, 1])

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved!")