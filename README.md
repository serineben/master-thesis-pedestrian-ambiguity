# Pedestrian Detection in Autonomous Driving using YOLOv8 and LLAVA

This repository contains the code and results from my **Master Thesis** project on pedestrian detection in urban driving scenarios, comparing **YOLOv8** and **LLAVA** for handling ambiguous situations.

---

## 📋 Project Overview

The goal of this project is to detect pedestrians in complex urban environments, including partially occluded or visually ambiguous cases, using both classical object detection (YOLOv8) and advanced vision-language model analysis (LLAVA).

Key contributions:  
- Creation of a diverse dataset from multiple sources (own GoPro recordings, public pedestrian datasets, and university data).  
- Frame extraction and manual selection of frames containing people.  
- YOLOv8-based pedestrian detection with confidence-based classification.  
- LLAVA-based scene understanding and pedestrian verification.  
- Quantitative evaluation using confusion matrices, heatmaps, and performance metrics.

---

## 🗂 Repository Structure

master-thesis-pedestrian-ambiguity/
├── data/
│ └── dataset_person_summary.csv # Summary CSV (full data not included)
├── src/
│ ├── extraireframe.py # Frame extraction script
│ ├── image_selection.py # GUI tool for manual frame selection
│ ├── run_yolo_detection.py # YOLOv8 detection script
│ ├── real-time-yolo.py # Real-time YOLO demo
│ └── LLAVAselectiontheone.py # LLAVA scene analysis
├── results/
│ ├── false_positive1.jpg # Example false positive 1
│ ├── false_positive2.jpg # Example false positive 2
│ └── conclusion/
│ ├── YOLO_confusion_matrix.png
│ ├── LLAVA_confusion_matrix.png
│ ├── heatmap_yolo_vs_llava.png
│ └── summary_metrics.csv
├── README.md
└── merged_results.csv

> **Note:** The original image datasets and full results are not included due to large file size. The included CSV and selected illustrative images are sufficient to understand the workflow and outputs.

---

## 🛠 Pipeline

The project workflow is summarized in the following diagram:

![Pipeline](results/pipeline.png)

1. **Video Collection** – multiple sources including GoPro, Sydney University dataset.  
2. **Frame Extraction** – every 10 seconds using `extraireframe.py`.  
3. **Manual Selection** – using `image_selection.py` to select frames containing people.  
4. **YOLOv8 Detection** – detect pedestrians and classify confidence levels.  
5. **LLAVA Scene Analysis** – detailed verification and scene understanding.  
6. **Evaluation** – merge results and generate confusion matrices, heatmaps, and metrics.

---

## 📊 Results Examples

### False Positives Example

Illustration of cases where YOLOv8 incorrectly detected a person:

![False Positive 1](results/false_positive1.jpg)
![False Positive 2](results/false_positive2.jpg)

### Confusion Matrices & Heatmap

#### YOLO vs LLAVA Confusion Matrices

![YOLO Confusion Matrix](results/conclusion/YOLO_confusion_matrix.png)
![LLAVA Confusion Matrix](results/conclusion/LLAVA_confusion_matrix.png)

#### Normalized Heatmap

![YOLO vs LLAVA Heatmap](results/conclusion/heatmap_yolo_vs_llava.png)

---

## ⚙ How to Run

1. **Frame Extraction:**  
```bash
python src/extraireframe.py

2. **Manual Selection:**  
```bash
python src/image_selection.py

3. **YOLO Detection:**  
```bash
python src/run_yolo_detection.py

4. **LLAVA Analysis:**  
```bash
python src/LLAVAselectiontheone.py

5. **Evaluation & Metrics:**  
```bash
python src/final-conclusion.py

Ensure all dependencies are installed (OpenCV, PIL, ultralytics, pandas, seaborn, scikit-learn, tqdm).


🔗 Contact / LinkedIn

Connect with me on LinkedIn(#)

Feel free to reach out for collaboration or questions regarding the project.

