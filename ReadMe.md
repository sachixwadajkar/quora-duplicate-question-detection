# quora duplicate question detection

## Application Demo

![Streamlit Demo](images/streamlit%20demo.png)

## Model Evaluation

### Confusion Matrix

![Confusion Matrix](images/confusion%20matrix.png)

### Feature Importance

![Feature Importance](images/feature%20importance.png)

## Project Overview

This project detects whether two Quora questions are duplicates using NLP feature engineering and machine learning.

The solution performs feature extraction using text similarity metrics and predicts duplicate questions through a Random Forest model deployed with Streamlit.

---

## Features

- Question length extraction
- Word count features
- Fuzzy string similarity
- Token sort ratio
- Token set ratio
- Random Forest classification
- Streamlit deployment

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- FuzzyWuzzy
- Matplotlib
- Seaborn

---

## Dataset

Dataset used:

Quora Question Pairs Dataset

Target:

0 → Not Duplicate

1 → Duplicate

---

## Features Used

q1_len

q2_len

q1_words

q2_words

fuzz_ratio

token_sort

token_set

---

## Model Pipeline

Questions

↓

Feature Engineering

↓

Random Forest

↓

Prediction

↓

Streamlit App

---

## Results

Model evaluation performed using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Feature Importance

---

## Project Structure

quora-duplicate-question-detection/

│── app.py

│── quora.ipynb

│── README.md

│── requirements.txt

│── .gitignore

│

└── images/

    ├── confusion_matrix.png

    ├── feature_importance.png

    └── streamlit_demo.png
## Run Locally

Install dependencies:

pip install -r requirements.txt

Run application:

python -m streamlit run app.py

---

## Streamlit Demo

(Add screenshot here)

---

## Future Improvements

- TF-IDF embeddings
- BERT embeddings
- Transformer models
- Semantic similarity methods
