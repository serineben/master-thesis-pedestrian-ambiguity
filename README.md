# 🚶 Pedestrian Detection in Autonomous Driving using YOLOv8 & LLaVA

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8-blue?logo=opencv)](https://opencv.org/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/serine-benmohra-55715b33b)


This Master's Thesis project explores advanced pedestrian detection in urban driving scenarios using **YOLOv8** and **LLaVA**. The research focuses on handling challenging cases such as partial visibility, occlusions, and ambiguous pedestrian appearances to enhance autonomous driving safety.

---

## 📖 Abstract

Pedestrian detection remains a critical challenge in autonomous driving systems, particularly in complex urban environments. This thesis investigates the integration of **YOLOv8** for real-time object detection and **LLaVA** (Large Language-and-Vision Assistant) for contextual scene understanding to improve detection accuracy in ambiguous scenarios. The proposed approach demonstrates enhanced performance in identifying partially visible and occluded pedestrians compared to traditional methods.

---

## 📂 Repository Structure
```bash
master-thesis-pedestrian-ambiguity/
├── 📊 data/
│   └── dataset_person_summary.csv
├── 🔧 src/
│   ├── analyze_results.py
│   ├── image_selection.py
│   ├── run_yolo_detection.py
│   ├── real_time_yolo.py
│   └── extract_frames.py
│   └── llava_analysis.py
├── 📈 results/
│   ├── llava-results.csv
│   ├── merged-results.csv
│   ├── yolo-results.csv
│   └── conclusion/
│       ├── YOLO_confusion_matrix.png
│       ├── LLAVA_confusion_matrix.png
│       ├── heatmap_yolo_vs_llava.png
│       └── summary_metrics.csv
├── images/
│   ├── pipeline.png
│   ├── yolo_false_positive1.jpg
│   ├── yolo_false_positive2.jpg
├── 📄 thesis/
│   └── master_thesis_document.pdf
├── README.md
└── requirements.txt
```
> Note: Full datasets and extensive results are not included due to size constraints. Contact me for access to complete research materials.

---
**🛠️ Methodology**

**Pipeline Overview**
<img src="images/pipeline.png" alt="Research Pipeline" width="400" height="400"/>

🎬 Frame Extraction - Extract relevant frames from driving scenario videos

👁️ Manual Curation - Select frames containing pedestrians using interactive GUI

🤖 YOLOv8 Detection - Perform initial pedestrian detection using YOLOv8

🔍 LLaVA Analysis - Apply vision-language model for contextual understanding

📊 Comparative Evaluation - Analyze results using confusion matrices and heatmaps

---

## 📊 Key Results

### Detection Performance

The combined YOLOv8 + LLaVA approach shows significant improvement in handling ambiguous cases:

**Reduced false positives** in complex urban scenes

**Enhanced detection** of partially visible pedestrians

**Better contextual** understanding of occluded scenarios

**❌ False Positive Analysis**
Examples where YOLOv8 alone produces incorrect detections:

<img src="images/yolo_false_positive1.jpg" alt="False Positive Case 1" width="400"/> <img src="images/yolo_false_positive2.jpg" alt="False Positive Case 2" width="400"/>


**📈 Performance Metrics**
Comparative analysis of YOLOv8 and LLaVA performance:

<img src="results/conclusion/YOLO_confusion_matrix.png" alt="YOLO Confusion Matrix" width="400"/> <img src="results/conclusion/LLAVA_confusion_matrix.png" alt="LLaVA Confusion Matrix" width="400"/> 

---
### ⚙️ Installation & Usage
**Prerequisites**
```bash
# Clone repository
git clone https://github.com/serineben/master-thesis-pedestrian-ambiguity.git
cd master-thesis-pedestrian-ambiguity

# Install dependencies
pip install -r requirements.txt 
```

**Execution Pipeline** 
```bash
# Run the complete analysis pipeline
python src/extract_frames.py
python src/image_selection.py
python src/run_yolo_detection.py
python src/llava_analysis.py
python src/analyze_results.py

# For real-time demonstration
python src/real_time_yolo.py
```


## 👨‍🎓 Author

**Serine Benmohra**  
📧 serinebenmohra@gmail.com  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/serine-benmohra-55715b33b)  
🎓 Master's Student in Artificial Intelligence  
🏫 Universidad de Alicante  

*This Master's Thesis research focuses on pedestrian detection systems for autonomous vehicles.*

**📝 Citation**
If you use this work in your research, please cite:
```bash
@mastersthesis{benmohra2025pedestrian,
  title={Pedestrian Detection in Autonomous Driving using YOLOv8 and LLaVA},
  author={Benmohra, Serine},
  year={2025},
  school={Universidad de Alicante}
}
```














