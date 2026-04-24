# 📋 Task Assignment & Progress Tracker

**Project**: Spam/Ham Classifier  
**Duration**: 4 Minggu (4 People)  
**Last Updated**: [Update date]

---

## 🚀 MINGGU 1: Setup & Foundation

### ✅ Orang 1 - Data Engineer

| #             | Task                     | Status         | Due Date   | Notes                                      |
| ------------- | ------------------------ | -------------- | ---------- | ------------------------------------------ |
| 1.1           | Clone repo & setup venv  | ⬜ Not Started | W1-Mon     | `git clone`, `python3 -m venv venv`        |
| 1.2           | Prepare dataset (CSV)    | ⬜ Not Started | W1-Wed     | Minimum 1000+ messages, 2 columns          |
| 1.3           | Validate dataset quality | ⬜ Not Started | W1-Fri     | Check encoding, duplicates, missing values |
| **W1 Status** |                          | ⬜             | **W1-Fri** | **Deliverable**: `data/dataset.csv`        |

---

### ✅ Orang 2 - ML Engineer

| #             | Task                       | Status         | Due Date   | Notes                                  |
| ------------- | -------------------------- | -------------- | ---------- | -------------------------------------- |
| 2.1           | Research 3 algorithms      | ⬜ Not Started | W1-Wed     | NB, LogReg, SVM pros/cons              |
| 2.2           | Setup ML environment       | ⬜ Not Started | W1-Thu     | Verify sklearn, numpy installations    |
| 2.3           | Design hyperparameter plan | ⬜ Not Started | W1-Fri     | Document param combinations            |
| **W1 Status** |                            | ⬜             | **W1-Fri** | **Deliverable**: Research doc + config |

---

### ✅ Orang 3 - Backend Developer

| #             | Task                      | Status         | Due Date   | Notes                                         |
| ------------- | ------------------------- | -------------- | ---------- | --------------------------------------------- |
| 3.1           | Code preprocessor.py      | ⬜ Not Started | W1-Wed     | clean_text, remove_stopwords, preprocess      |
| 3.2           | Write unit tests          | ⬜ Not Started | W1-Thu     | 5+ test cases with pytest                     |
| 3.3           | Code review documentation | ⬜ Not Started | W1-Fri     | Docstrings, inline comments                   |
| **W1 Status** |                           | ⬜             | **W1-Fri** | **Deliverable**: `src/preprocessor.py` tested |

---

### ✅ Orang 4 - DevOps/QA

| #             | Task                            | Status         | Due Date   | Notes                                       |
| ------------- | ------------------------------- | -------------- | ---------- | ------------------------------------------- |
| 4.1           | Setup git workflow              | ⬜ Not Started | W1-Wed     | .gitignore, branch strategy                 |
| 4.2           | Create collaboration guidelines | ⬜ Not Started | W1-Thu     | CONTRIBUTING.md, PR template                |
| 4.3           | QA checklist & tracker          | ⬜ Not Started | W1-Fri     | Testing procedures                          |
| **W1 Status** |                                 | ⬜             | **W1-Fri** | **Deliverable**: Git configured, docs ready |

---

## 📊 MINGGU 2: Data Analysis

### ✅ Orang 1 - Data Engineer 🔴 PRIMARY

| #             | Task                   | Status         | Due Date   | Notes                                                 |
| ------------- | ---------------------- | -------------- | ---------- | ----------------------------------------------------- |
| 1.4           | Complete 01_eda.ipynb  | ⬜ Not Started | W2-Thu     | Load, clean, analyze data                             |
| 1.5           | Generate statistics    | ⬜ Not Started | W2-Wed     | Descriptive stats, profiling                          |
| 1.6           | Save dataset_clean.csv | ⬜ Not Started | W2-Fri     | **Pass to Orang 2**                                   |
| **W2 Status** |                        | ⬜             | **W2-Fri** | **Deliverable**: `01_eda.ipynb` + `dataset_clean.csv` |

---

### ✅ Orang 2 - ML Engineer

| #             | Task                       | Status         | Due Date   | Notes                                  |
| ------------- | -------------------------- | -------------- | ---------- | -------------------------------------- |
| 2.4           | EDA visualization design   | ⬜ Not Started | W2-Mon     | Coordinate with Orang 1                |
| 2.5           | Model training preparation | ⬜ Not Started | W2-Wed     | Pipeline setup, split strategy         |
| 2.6           | Cross-validation setup     | ⬜ Not Started | W2-Fri     | StratifiedKFold, metrics               |
| **W2 Status** |                            | ⬜             | **W2-Fri** | **Deliverable**: Training ready for W3 |

---

### ✅ Orang 3 - Backend Developer

| #             | Task                     | Status         | Due Date   | Notes                                   |
| ------------- | ------------------------ | -------------- | ---------- | --------------------------------------- |
| 3.4           | Integrate preprocessing  | ⬜ Not Started | W2-Wed     | Test with EDA notebook                  |
| 3.5           | Create utility functions | ⬜ Not Started | W2-Thu     | data loading, visualization helpers     |
| 3.6           | Error handling & logging | ⬜ Not Started | W2-Fri     | Try-catch, validation                   |
| **W2 Status** |                          | ⬜             | **W2-Fri** | **Deliverable**: Utils & error handling |

---

### ✅ Orang 4 - DevOps/QA

| #             | Task                  | Status         | Due Date   | Notes                                  |
| ------------- | --------------------- | -------------- | ---------- | -------------------------------------- |
| 4.4           | Test data preparation | ⬜ Not Started | W2-Wed     | Validate CSV format, integrity         |
| 4.5           | Documentation update  | ⬜ Not Started | W2-Thu     | Update README, naming conventions      |
| 4.6           | Backup & versioning   | ⬜ Not Started | W2-Fri     | DVC setup, procedures                  |
| **W2 Status** |                       | ⬜             | **W2-Fri** | **Deliverable**: Data & docs validated |

---

## 🤖 MINGGU 3: Model Training

### ✅ Orang 1 - Data Engineer

| #             | Task                     | Status         | Due Date   | Notes                             |
| ------------- | ------------------------ | -------------- | ---------- | --------------------------------- |
| 1.7           | Prepare training dataset | ⬜ Not Started | W3-Mon     | Handle imbalance, final split     |
| 1.8           | Data monitoring setup    | ⬜ Not Started | W3-Wed     | Logging, tracking                 |
| 1.9           | Support ML Engineer      | ⬜ Not Started | W3-Fri     | Assist with data issues           |
| **W3 Status** |                          | ⬜             | **W3-Fri** | **Deliverable**: Training support |

---

### ✅ Orang 2 - ML Engineer 🔴 PRIMARY

| #             | Task                       | Status         | Due Date   | Notes                                             |
| ------------- | -------------------------- | -------------- | ---------- | ------------------------------------------------- |
| 2.7           | Train 3 models             | ⬜ Not Started | W3-Tue     | NB, LogReg, SVM                                   |
| 2.8           | Complete 02_training.ipynb | ⬜ Not Started | W3-Wed     | Evaluation, comparison                            |
| 2.9           | Hyperparameter tuning      | ⬜ Not Started | W3-Thu     | GridSearch/RandomSearch                           |
| 2.10          | Select best model          | ⬜ Not Started | W3-Fri     | **Pass to Orang 3**                               |
| **W3 Status** |                            | ⬜             | **W3-Fri** | **Deliverable**: `02_training.ipynb` + best model |

---

### ✅ Orang 3 - Backend Developer

| #             | Task                     | Status         | Due Date   | Notes                                      |
| ------------- | ------------------------ | -------------- | ---------- | ------------------------------------------ |
| 3.7           | Code predictor.py        | ⬜ Not Started | W3-Wed     | SpamHamPredictor class                     |
| 3.8           | Integration testing      | ⬜ Not Started | W3-Thu     | Test with trained model                    |
| 3.9           | Performance optimization | ⬜ Not Started | W3-Fri     | Latency, memory                            |
| **W3 Status** |                          | ⬜             | **W3-Fri** | **Deliverable**: `src/predictor.py` tested |

---

### ✅ Orang 4 - DevOps/QA

| #             | Task                     | Status         | Due Date   | Notes                          |
| ------------- | ------------------------ | -------------- | ---------- | ------------------------------ |
| 4.7           | Model validation testing | ⬜ Not Started | W3-Wed     | File integrity, loading        |
| 4.8           | Performance benchmarking | ⬜ Not Started | W3-Thu     | Speed, memory tests            |
| 4.9           | Documentation update     | ⬜ Not Started | W3-Fri     | Model specs, performance       |
| **W3 Status** |                          | ⬜             | **W3-Fri** | **Deliverable**: Model reports |

---

## 🎯 MINGGU 4: Testing & Release

### ✅ Orang 1 - Data Engineer

| #             | Task                  | Status         | Due Date   | Notes                            |
| ------------- | --------------------- | -------------- | ---------- | -------------------------------- |
| 1.10          | Create test dataset   | ⬜ Not Started | W4-Tue     | Diverse test messages            |
| 1.11          | Final data validation | ⬜ Not Started | W4-Wed     | Data leakage check               |
| **W4 Status** |                       | ⬜             | **W4-Wed** | **Deliverable**: Test data ready |

---

### ✅ Orang 2 - ML Engineer

| #             | Task                     | Status         | Due Date   | Notes                          |
| ------------- | ------------------------ | -------------- | ---------- | ------------------------------ |
| 2.11          | Model documentation      | ⬜ Not Started | W4-Tue     | Model card, feature importance |
| 2.12          | Polish 02_training.ipynb | ⬜ Not Started | W4-Wed     | Comments, viz, interpretation  |
| **W4 Status** |                          | ⬜             | **W4-Wed** | **Deliverable**: Doc complete  |

---

### ✅ Orang 3 - Backend Developer 🔴 PRIMARY

| #             | Task                         | Status         | Due Date   | Notes                                           |
| ------------- | ---------------------------- | -------------- | ---------- | ----------------------------------------------- |
| 3.10          | Complete 03_prediction.ipynb | ⬜ Not Started | W4-Tue     | Single/batch prediction, interactive            |
| 3.11          | Integration testing          | ⬜ Not Started | W4-Wed     | End-to-end tests                                |
| 3.12          | Code review & refactor       | ⬜ Not Started | W4-Thu     | Readability, final polish                       |
| **W4 Status** |                              | ⬜             | **W4-Thu** | **Deliverable**: `03_prediction.ipynb` complete |

---

### ✅ Orang 4 - DevOps/QA 🔴 PRIMARY

| #             | Task                 | Status         | Due Date   | Notes                                       |
| ------------- | -------------------- | -------------- | ---------- | ------------------------------------------- |
| 4.10          | System testing       | ⬜ Not Started | W4-Mon     | All 3 notebooks end-to-end                  |
| 4.11          | Final documentation  | ⬜ Not Started | W4-Wed     | README, quick start, troubleshoot           |
| 4.12          | Release preparation  | ⬜ Not Started | W4-Thu     | Code review, cleanup, release notes         |
| 4.13          | Project presentation | ⬜ Not Started | W4-Fri     | Summary, demo, lessons learned              |
| **W4 Status** |                      | ⬜             | **W4-Fri** | **FINAL DELIVERABLE**: Production-ready! ✨ |

---

## 📊 Status Legend

- ⬜ Not Started
- 🟨 In Progress
- 🟩 Completed
- 🔴 Blocked/Issue

---

## 🚨 Blockers & Issues

| Issue     | Owner    | Status  | Resolution |
| --------- | -------- | ------- | ---------- |
| [Issue 1] | [Person] | ⬜ Open | [Solution] |
| [Issue 2] | [Person] | ⬜ Open | [Solution] |

---

## ✅ Final Checklist (W4-Fri)

- [ ] All 3 notebooks complete & functional
- [ ] All unit tests passing
- [ ] End-to-end prediction working
- [ ] Model accuracy > 90%
- [ ] Documentation complete
- [ ] .gitignore properly configured
- [ ] README updated with all steps
- [ ] Project tested on multiple systems
- [ ] Code reviewed & approved
- [ ] Ready for deployment ✨

---

**Project Manager**: [Name]  
**Last Updated**: [Date/Time]  
**Next Standup**: [Date/Time]
