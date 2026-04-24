# 🚀 Quick Reference: 4 Minggu Project Plan

## Tim (4 Orang)

| Orang       | Role          | Minggu 1        | Minggu 2     | Minggu 3        | Minggu 4      |
| ----------- | ------------- | --------------- | ------------ | --------------- | ------------- |
| **Orang 1** | Data Engineer | Setup + Dataset | EDA Notebook | Data Split      | Test Data     |
| **Orang 2** | ML Engineer   | Research        | CV Setup     | Train Models    | Doc & Polish  |
| **Orang 3** | Backend Dev   | Preprocessor    | Integration  | Predictor Class | Prediction NB |
| **Orang 4** | DevOps/QA     | Git Setup       | QA & Docs    | Validation      | Final Testing |

---

## 📊 Minggu 1: Foundation

### Orang 1 → Data Engineer

1. Clone repo & setup venv
2. **Prepare dataset** (`data/dataset.csv`)
3. Initial data exploration

### Orang 2 → ML Engineer

1. Research 3 models (NB, LogReg, SVM)
2. Setup ML environment
3. Design hyperparameter plan

### Orang 3 → Backend Developer

1. **Code `preprocessor.py`** (clean_text, remove_stopwords, preprocess)
2. Write unit tests
3. Documentation

### Orang 4 → DevOps/QA

1. **Setup git workflow** (.gitignore, branch strategy)
2. Create collaboration guidelines
3. QA checklist

**🎯 Deliverables**: Dataset ready, Preprocessor tested, Git configured

---

## 📊 Minggu 2: Data Analysis

### Orang 1 → Data Engineer 🔴 LEAD

1. **Complete `01_eda.ipynb`**
2. Label distribution analysis
3. **Save `dataset_clean.csv`** ← Pass to Orang 2

### Orang 2 → ML Engineer

1. Design EDA visualizations (coordinate dengan Orang 1)
2. Setup model pipeline templates
3. Prepare cross-validation

### Orang 3 → Backend Developer

1. Integrate preprocessing into EDA
2. Create utility functions
3. Add error handling

### Orang 4 → DevOps/QA

1. Validate dataset format
2. Update documentation
3. Setup data versioning

**🎯 Deliverables**: `01_eda.ipynb` complete, `dataset_clean.csv` ready

---

## 📊 Minggu 3: Model Development

### Orang 1 → Data Engineer

1. Final train/test split
2. Data monitoring setup
3. Support ML training

### Orang 2 → ML Engineer 🔴 LEAD

1. **Train 3 models** (NB, LogReg, SVM)
2. **Complete `02_training.ipynb`**
3. Hyperparameter tuning
4. **Select best model** ← Pass to Orang 3

### Orang 3 → Backend Developer

1. **Code `predictor.py`** (SpamHamPredictor class)
2. Integration testing
3. Performance optimization

### Orang 4 → DevOps/QA

1. Model validation testing
2. Performance benchmarking
3. Update documentation

**🎯 Deliverables**: `02_training.ipynb` complete, trained model saved, predictor class ready

---

## 📊 Minggu 4: Testing & Release

### Orang 1 → Data Engineer

1. Create test dataset
2. Final data validation

### Orang 2 → ML Engineer

1. Model documentation
2. Finalize training notebook

### Orang 3 → Backend Developer 🔴 LEAD

1. **Complete `03_prediction.ipynb`**
2. Single + batch prediction
3. Integration testing

### Orang 4 → DevOps/QA 🔴 LEAD

1. **End-to-end system testing**
2. **Complete final documentation**
3. Release preparation

**🎯 Deliverables**: 3 Notebooks complete, Full documentation, Production-ready! ✨

---

## 🎯 Key Dependencies

```
Minggu 1:  Setup ✓
           ↓
Minggu 2:  Dataset Ready (Orang 1)
           ↓
Minggu 3:  Cleaned Data (Orang 1) + Predictor (Orang 3)
           ↓
Minggu 4:  Final Testing & Release
```

---

## ✅ Final Deliverables

```
📁 spam-ham-classifier/
├── 📓 notebooks/
│   ├── 01_eda.ipynb          ← Orang 1 (Minggu 2)
│   ├── 02_training.ipynb     ← Orang 2 (Minggu 3)
│   └── 03_prediction.ipynb   ← Orang 3 (Minggu 4)
├── 🐍 src/
│   ├── preprocessor.py       ← Orang 3 (Minggu 1) ✓
│   └── predictor.py          ← Orang 3 (Minggu 3)
├── 📊 data/
│   ├── dataset.csv           ← Orang 1 (Minggu 1) ✓
│   └── dataset_clean.csv     ← Orang 1 (Minggu 2)
├── 🤖 models/
│   ├── spam_ham_model.pkl    ← Orang 2 (Minggu 3)
│   └── model_info.json       ← Orang 2 (Minggu 3)
├── 📚 README.md              ← Orang 4 (Minggu 4)
├── 📋 PROJECT_PLAN.md        ← Orang 4 (Minggu 4)
└── .gitignore                ← Orang 4 (Minggu 1) ✓
```

---

## 💬 Communication Tips

- **Daily Updates**: Slack/Teams dengan blockers
- **Weekly Standup**: 30 min sync call
- **GitHub Issues**: Track blockers & dependencies
- **Code Review**: All PRs reviewed before merge
- **Escalate Early**: Don't wait if stuck!
