Machine Learning Based Intrusion Detection System (IDS)
Project Overview

This project implements a Machine Learning-based Intrusion Detection System (IDS) to classify network traffic as:

Normal (0)

Attack (1)

The system is built using the NSL-KDD dataset and focuses on optimizing the precision-recall tradeoff, which is critical in real-world cybersecurity systems.

Problem Statement

Traditional signature-based IDS systems fail to detect new or unknown attacks.

This project builds a supervised machine learning model capable of:

Detecting malicious traffic

Reducing False Negatives (missed attacks)

Maintaining a balance between precision and recall

Special emphasis was placed on minimizing False Negatives, as missed attacks can lead to:

Data breaches

Financial loss

Confidentiality compromise

System exploitation

📊 Dataset Used

Dataset: NSL-KDD

The dataset contains:

41 network traffic features

Various attack types

Label column

Difficulty level column

For this project:

Multi-class labels were converted into binary:

0 → Normal

1 → Attack

Difficulty column was removed

Technologies Used

Python

Pandas

NumPy

Scikit-learn

Random Forest Classifier

⚙️ Methodology

1️⃣ Data Preprocessing

Loaded training and testing datasets

Converted labels to binary classification

Removed unnecessary column (difficulty)

Separated features (X) and target (y)

2️⃣ Feature Engineering

One-hot encoding for categorical features:

protocol_type

service

flag

Aligned training and testing feature columns

3️⃣ Model Building

Used:

RandomForestClassifier(
    n_estimators=500,
    min_samples_split=5,
    min_samples_leaf=2,
    class_weight={0:1, 1:5},
    random_state=42
)

4️⃣ Handling Class Imbalance

Applied class weighting to increase importance of attack class

Tuned prediction threshold (0.22) to improve recall

5️⃣ Evaluation Metrics

Confusion Matrix

Precision

Recall

F1-score

Accuracy

📈 Final Results

Accuracy: 87%

Confusion Matrix:
[[ 9324   387]
 [ 2655 10178]]
Performance:
Metric	Normal	Attack
Precision	0.78	0.96
Recall	0.96	0.79
F1-score	0.86	0.87
🔍 Security Tradeoff Analysis

In cybersecurity systems:

False Negative (FN) is more dangerous than False Positive.

Missing an attack can cause major damage.

Therefore, recall for attack detection was prioritized.

Threshold tuning was applied to balance:

High recall for attack detection

Acceptable false positive rate

🚀 Key Learnings

Importance of precision-recall tradeoff in IDS

Handling class imbalance using class_weight

Preventing data leakage during preprocessing

Threshold tuning for security-sensitive applications

Real-world model evaluation strategy

📎 How to Run

Download NSL-KDD dataset

Place dataset files in project folder

Install dependencies:

pip install -r requirements.txt

Run:

python IDS_model.py"# ML-Based-Intrusion-Detection-System" 


