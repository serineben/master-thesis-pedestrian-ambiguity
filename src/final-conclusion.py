import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, f1_score, accuracy_score
from pathlib import Path
import os
import numpy as np
# === CONFIG ===
INPUT_CSV = "merged_results.csv"  # Your CSV file
OUTPUT_DIR = Path("conclusion1")
OUTPUT_DIR.mkdir(exist_ok=True)

# === LOAD DATA ===
df = pd.read_csv(INPUT_CSV)

# === BINARIZE DATA ===
df["gt_person"] = df["true_person_count"] > 0
df["yolo_detected"] = df["yolo_count"] > 0
df["llava_detected"] = df["llava_count"] > 0

# === FUNCTION TO PLOT AND SAVE CONFUSION MATRIX ===
def plot_and_save_confusion_matrix(y_true, y_pred, model_name):
    cm = confusion_matrix(y_true, y_pred)
    # Convert counts to percentages
    cm_percent = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
    
    disp = ConfusionMatrixDisplay(confusion_matrix=cm_percent, 
                                display_labels=["No Person", "Person"])
    fig, ax = plt.subplots(figsize=(6,6))
    disp.plot(ax=ax, cmap="Blues", values_format=".1f")  # 1 decimal place
    plt.title(f"{model_name} Confusion Matrix (%)\n(rows sum to 100%)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"{model_name}_confusion_matrix_percent.png")
    plt.close(fig)
    return cm

# === PLOT CONFUSION MATRICES ===
cm_yolo = plot_and_save_confusion_matrix(df["gt_person"], df["yolo_detected"], "YOLO")
cm_llava = plot_and_save_confusion_matrix(df["gt_person"], df["llava_detected"], "LLAVA")

# === HEATMAP FOR YOLO VS LLAVA PERSON COUNTS ===
pivot = df.pivot_table(index="yolo_count", columns="llava_count", aggfunc="size", fill_value=0)
pivot_norm = pivot.div(pivot.sum(axis=1), axis=0).fillna(0)

plt.figure(figsize=(12,8))
sns.heatmap(pivot_norm, annot=True, fmt=".1%", cmap="YlOrRd")
plt.title("Normalized Heatmap: YOLO Count vs LLAVA Count")
plt.xlabel("LLAVA Person Count")
plt.ylabel("YOLO Person Count")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "heatmap_yolo_vs_llava.png")
plt.close()

# === CALCULATE METRICS ===
def compute_metrics(y_true, y_pred):
    return {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred),
        "Recall": recall_score(y_true, y_pred),
        "F1-Score": f1_score(y_true, y_pred)
    }

metrics_yolo = compute_metrics(df["gt_person"], df["yolo_detected"])
metrics_llava = compute_metrics(df["gt_person"], df["llava_detected"])

# === CREATE SUMMARY FILE ===
summary_df = pd.DataFrame([metrics_yolo, metrics_llava], index=["YOLO", "LLAVA"])
summary_df.to_csv(OUTPUT_DIR / "summary_metrics.csv")

# === PRINT SUMMARY TO TERMINAL ===
print("=== Metrics Summary ===")
print(summary_df)

print(f"\nResults have been saved in the folder: {OUTPUT_DIR.resolve()}")
