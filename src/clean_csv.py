import pandas as pd

# Path to your CSV file
file_path = "../results/yolo_results.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Replace all occurrences of "_nv" in all string columns
df = df.replace(to_replace=r'_nv', value='', regex=True)

# Save the cleaned version (overwrite or create a new one)
df.to_csv("../results/yolo-results.csv", index=False)

print("✅ Cleaning done! New file saved as yolo-results.csv")
