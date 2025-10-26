# 🚶 Pedestrian Detection in Autonomous Driving using YOLOv8 & LLaVA

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8-blue?logo=opencv)](https://opencv.org/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/serine-benmohra-55715b33b)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

This Master's Thesis project explores advanced pedestrian detection in urban driving scenarios using **YOLOv8** and **LLaVA**. The research focuses on handling challenging cases such as partial visibility, occlusions, and ambiguous pedestrian appearances to enhance autonomous driving safety.

---

## 📖 Abstract

Pedestrian detection remains a critical challenge in autonomous driving systems, particularly in complex urban environments. This thesis investigates the integration of **YOLOv8** for real-time object detection and **LLaVA** (Large Language-and-Vision Assistant) for contextual scene understanding to improve detection accuracy in ambiguous scenarios. The proposed approach demonstrates enhanced performance in identifying partially visible and occluded pedestrians compared to traditional methods.

---

## 📂 Repository Structure

master-thesis-pedestrian-ambiguity/
├── 📊 data/
│   └── dataset_person_summary.csv
├── 🔧 src/
│   ├── extraireframe.py
│   ├── image_selection.py
│   ├── run_yolo_detection.py
│   ├── real-time-yolo.py
│   └── LLAVAselectiontheone.py
├── 📈 results/
│   ├── pipeline.png
│   ├── false_positive1.jpg
│   ├── false_positive2.jpg
│   └── conclusion/
│       ├── YOLO_confusion_matrix.png
│       ├── LLAVA_confusion_matrix.png
│       ├── heatmap_yolo_vs_llava.png
│       └── summary_metrics.csv
├── 📄 thesis/
│   └── master_thesis_document.pdf
├── README.md
└── requirements.txt

> ⚠️ Full datasets and complete results are not included due to size constraints.

---

## 🛠 Pipeline

<img src="images/pipeline.png" alt="Pipeline" width="600"/>

1. 🎬 Extract frames from videos.  
2. 👁️ Manually select frames with pedestrians.  
3. 🤖 Detect pedestrians using YOLOv8.  
4. 🔍 Analyze scenes with LLAVA.  
5. 📊 Evaluate results with confusion matrices & heatmaps.

---

## 📊 Results Examples

### ❌ False Positives

Examples of YOLOv8 mistakes:

<img src="images/yolo_false_positive1.jpg" alt="False Positive 1" width="400"/>
<img src="images/yolo_false_positive2.jpg" alt="False Positive 2" width="400"/>

### 📈 Confusion Matrices & Heatmap

<img src="results/conclusion/YOLO_confusion_matrix.png" alt="YOLO Confusion Matrix" width="400"/>
<img src="results/conclusion/LLAVA_confusion_matrix.png" alt="LLAVA Confusion Matrix" width="400"/>
<img src="results/conclusion/heatmap_yolo_vs_llava.png" alt="YOLO vs LLAVA Heatmap" width="400"/>

---

## ⚙ How to Run

```bash
python src/extract_frames.py
python src/image_selection.py
python src/run_yolo_detection.py
python src/llava_analysis.py
python src/analyze_results.py








