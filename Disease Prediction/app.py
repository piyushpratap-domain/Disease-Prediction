import pandas as pd

data = pd.read_csv("Training.csv")
print(f"Total diseases: {data['prognosis'].nunique()}")  # Verify 41 diseases
print(data.head())
print(data["prognosis"].value_counts().plot(kind='bar', figsize=(12, 4)))
