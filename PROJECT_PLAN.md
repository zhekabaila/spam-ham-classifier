# 📅 Project Plan: Spam/Ham Classifier — 4 Minggu, 4 Orang

## 📊 Ringkasan Umum

| Aspek                 | Detail                                     |
| --------------------- | ------------------------------------------ |
| **Durasi**            | 4 minggu                                   |
| **Tim**               | 4 orang (Orang 1-4)                        |
| **Deliverable Utama** | Model ML, 3 Jupyter Notebooks, Dokumentasi |
| **Staging**           | Development → Testing → Deployment         |

---

## 👥 Pembagian Tim & Role

| Role                  | Orang   | Responsibilitas                                    |
| --------------------- | ------- | -------------------------------------------------- |
| **Data Engineer**     | Orang 1 | Dataset preparation, data cleaning, EDA            |
| **ML Engineer**       | Orang 2 | Model training, evaluation, hyperparameter tuning  |
| **Backend Developer** | Orang 3 | Preprocessing module, prediction class, testing    |
| **DevOps / QA**       | Orang 4 | Setup infrastructure, documentation, final testing |

---

## 📋 Timeline Detil (4 Minggu)

### 🏁 MINGGU 1: Setup & Data Preparation

#### **Orang 1 - Data Engineer**

- **Task 1.1**: Setup development environment
  - Clone repository dari GitHub
  - Setup virtual environment (`venv`)
  - Install dependencies dari `requirements.txt`
  - **Deliverable**: Screenshot environment setup + verified dependencies
- **Task 1.2**: Prepare dan validate dataset
  - Kumpulkan dataset spam/ham yang akan digunakan
  - Ensure format CSV dengan kolom: `kategori`, `pesan`
  - Validate data quality (ukuran, encoding, duplikasi)
  - **Deliverable**: `data/dataset.csv` (minimal 1000-5000 records)

- **Task 1.3**: Initial data exploration
  - Load dataset menggunakan pandas
  - Check shape, dtypes, missing values
  - Create quick summary statistics
  - **Deliverable**: Jupyter notebook dengan exploratory code

- **Deadline**: Akhir Minggu 1 (dataset ready untuk Week 2)

---

#### **Orang 2 - ML Engineer**

- **Task 2.1**: Research model architecture
  - Riset 3 algoritma: Naive Bayes, Logistic Regression, Linear SVM
  - Dokumentasi algoritma + pros/cons
  - Decision pada TF-IDF untuk feature extraction
  - **Deliverable**: Research document (1-2 pages)

- **Task 2.2**: Setup ML environment
  - Verify scikit-learn, numpy, pandas installations
  - Test import semua ML libraries
  - Create test script untuk model training
  - **Deliverable**: Test script yang bisa run successfully

- **Task 2.3**: Design model pipeline
  - Plan hyperparameter combinations
  - Design cross-validation strategy (5-fold)
  - Create model evaluation metrics plan
  - **Deliverable**: Hyperparameter config file

- **Deadline**: Akhir Minggu 1

---

#### **Orang 3 - Backend Developer**

- **Task 3.1**: Implement `preprocessor.py`
  - Code `clean_text()` function
  - Code `remove_stopwords()` function
  - Code `preprocess()` pipeline
  - Add unit tests untuk setiap function
  - **Deliverable**: Complete `src/preprocessor.py` + test_preprocessor.py

- **Task 3.2**: Setup testing framework
  - Install pytest
  - Create test file structure
  - Write 5+ test cases untuk preprocessing functions
  - **Deliverable**: `tests/test_preprocessor.py` dengan passing tests

- **Task 3.3**: Code review documentation
  - Document preprocessing pipeline
  - Create function docstrings
  - Prepare code review checklist
  - **Deliverable**: Detailed code documentation

- **Deadline**: Akhir Minggu 1

---

#### **Orang 4 - DevOps / QA**

- **Task 4.1**: Setup git workflow
  - Configure branch strategy (main, develop, feature branches)
  - Create .gitignore dengan rules yang tepat
  - Setup GitHub Actions (optional)
  - **Deliverable**: Git workflow documentation + .gitignore

- **Task 4.2**: Infrastructure & documentation setup
  - Create project documentation structure
  - Setup Wiki/document repository
  - Create collaboration guidelines
  - **Deliverable**: `CONTRIBUTING.md`, project guidelines

- **Task 4.3**: Quality assurance checklist
  - Create QA testing checklist
  - Prepare test environment
  - Create progress tracking sheet
  - **Deliverable**: QA checklist, progress tracker

- **Deadline**: Akhir Minggu 1

---

### 📊 MINGGU 2: Exploratory Data Analysis (EDA)

#### **Orang 1 - Data Engineer** 🎯 LEAD

- **Task 1.4**: Complete EDA notebook (`01_eda.ipynb`)
  - Load clean dataset
  - Check missing values & duplicates
  - Analyze label distribution (bar + pie charts)
  - Analyze message length statistics
  - Apply preprocessing to all messages
  - **Deliverable**: Complete `notebooks/01_eda.ipynb` + visualizations

- **Task 1.5**: Data profiling & statistics
  - Generate descriptive statistics
  - Create data profile report
  - Identify data quality issues
  - **Deliverable**: Data profile document

- **Task 1.6**: Save cleaned dataset
  - Export cleaned dataset → `data/dataset_clean.csv`
  - Create data dictionary
  - Verify no data loss
  - **Deliverable**: `data/dataset_clean.csv` + data dictionary

- **Collaboration**: Share cleaned dataset dengan Orang 2 untuk training
- **Deadline**: Tengah-akhir Minggu 2

---

#### **Orang 2 - ML Engineer**

- **Task 2.4**: EDA visualization design
  - Collaborate dengan Orang 1 untuk visualization requirements
  - Design plots untuk label distribution
  - Design plots untuk feature statistics
  - **Deliverable**: Visualization specs

- **Task 2.5**: Model training preparation
  - Prepare TF-IDF vectorizer config
  - Setup pipeline templates
  - Prepare train/test split strategy
  - **Deliverable**: Model training script template

- **Task 2.6**: Cross-validation setup
  - Implement StratifiedKFold validation
  - Prepare evaluation metrics calculation
  - Create results tracking sheet
  - **Deliverable**: CV implementation + metrics script

- **Collaboration**: Tunggu cleaned dataset dari Orang 1
- **Deadline**: Akhir Minggu 2 (siap untuk Week 3 training)

---

#### **Orang 3 - Backend Developer**

- **Task 3.4**: Integrate preprocessing ke EDA notebook
  - Embed `preprocess()` function calls di notebook
  - Test preprocessing pada sample data
  - Fix any preprocessing issues
  - **Deliverable**: Tested preprocessing integration

- **Task 3.5**: Create utility functions
  - Helper functions untuk data loading
  - Helper functions untuk visualization
  - Utility untuk path management
  - **Deliverable**: `src/utils.py` dengan helper functions

- **Task 3.6**: Add error handling
  - Add try-catch blocks untuk file operations
  - Add data validation functions
  - Add logging setup
  - **Deliverable**: Robust error handling implementation

- **Deadline**: Akhir Minggu 2

---

#### **Orang 4 - DevOps / QA**

- **Task 4.4**: Test data preparation
  - Validate dataset format
  - Check CSV integrity
  - Verify column names & data types
  - **Deliverable**: Data validation report

- **Task 4.5**: Documentation update
  - Update README dengan Minggu 2 progress
  - Document EDA findings template
  - Create visualization naming conventions
  - **Deliverable**: Updated documentation

- **Task 4.6**: Backup & versioning
  - Setup data versioning (DVC optional)
  - Create backup procedures
  - Version control best practices
  - **Deliverable**: Versioning documentation

- **Deadline**: Akhir Minggu 2

---

### 🤖 MINGGU 3: Model Training & Evaluation

#### **Orang 1 - Data Engineer**

- **Task 1.7**: Prepare final training dataset
  - Handle class imbalance (if any)
  - Create train/val/test splits
  - Document data split ratios
  - **Deliverable**: Verified train/test split data

- **Task 1.8**: Data monitoring & logging
  - Setup data logging untuk training process
  - Monitor data distribution during training
  - Track data-related issues
  - **Deliverable**: Data logging implementation

- **Task 1.9**: Support ML Engineer
  - Assist dengan data issues during training
  - Handle edge cases dalam data
  - Provide data insights untuk model tuning
  - **Deliverable**: Data analysis support

- **Deadline**: Throughout Minggu 3

---

#### **Orang 2 - ML Engineer** 🎯 LEAD

- **Task 2.7**: Train 3 models
  - Train Naive Bayes model
  - Train Logistic Regression model
  - Train Linear SVM model
  - Track training metrics untuk setiap model
  - **Deliverable**: 3 trained models

- **Task 2.8**: Model evaluation & comparison
  - Calculate accuracy, precision, recall, F1
  - Cross-validation scoring (5-fold)
  - Generate confusion matrices
  - Compare model performance
  - **Deliverable**: Complete `notebooks/02_training.ipynb`

- **Task 2.9**: Hyperparameter tuning
  - Test multiple hyperparameter combinations
  - GridSearch atau RandomSearch
  - Document best hyperparameters
  - **Deliverable**: Tuning results & best params

- **Task 2.10**: Select best model
  - Choose best model berdasarkan CV F1 score
  - Verify model robustness
  - Document model selection rationale
  - **Deliverable**: Final trained model file

- **Collaboration**: Work closely dengan Orang 1 (data) dan Orang 3 (preprocessing)
- **Deadline**: Akhir Minggu 3

---

#### **Orang 3 - Backend Developer**

- **Task 3.7**: Implement `predictor.py`
  - Code `SpamHamPredictor` class
  - Implement `predict()` method
  - Implement `predict_batch()` method
  - Implement `display_result()` method
  - **Deliverable**: Complete `src/predictor.py`

- **Task 3.8**: Integration testing
  - Test predictor dengan trained model
  - Test error handling & edge cases
  - Test batch prediction
  - Write unit tests untuk predictor
  - **Deliverable**: `tests/test_predictor.py` + passing tests

- **Task 3.9**: Performance optimization
  - Profile predictor performance
  - Optimize prediction latency
  - Memory usage optimization
  - **Deliverable**: Performance report

- **Collaboration**: Integrate trained model dari Orang 2
- **Deadline**: Akhir Minggu 3

---

#### **Orang 4 - DevOps / QA**

- **Task 4.7**: Model validation testing
  - Test trained model loading
  - Verify model file integrity
  - Test model versioning
  - **Deliverable**: Model validation report

- **Task 4.8**: Performance benchmarking
  - Benchmark model inference speed
  - Test memory usage
  - Test on different data sizes
  - **Deliverable**: Benchmarking report

- **Task 4.9**: Documentation update
  - Update README dengan model info
  - Document model training process
  - Create model performance report
  - **Deliverable**: Model documentation

- **Deadline**: Akhir Minggu 3

---

### 🎯 MINGGU 4: Prediction Interface & Final Testing

#### **Orang 1 - Data Engineer**

- **Task 1.10**: Create test dataset
  - Prepare diverse test messages
  - Create expected classification labels
  - Document test scenarios
  - **Deliverable**: `tests/test_messages.csv`

- **Task 1.11**: Final data validation
  - Validate all datasets used
  - Check for data leakage
  - Verify data consistency
  - **Deliverable**: Final data validation report

- **Deadline**: Mid-Minggu 4

---

#### **Orang 2 - ML Engineer**

- **Task 2.11**: Model documentation
  - Document model architecture
  - Create model card (model specs)
  - Explain feature importance
  - **Deliverable**: Model documentation

- **Task 2.12**: Finalize `02_training.ipynb`
  - Add explanatory comments
  - Add performance visualization
  - Add interpretation guide
  - **Deliverable**: Final polished notebook

- **Deadline**: Mid-Minggu 4

---

#### **Orang 3 - Backend Developer** 🎯 LEAD

- **Task 3.10**: Create prediction interface notebook (`03_prediction.ipynb`)
  - Load model menggunakan predictor class
  - Implement single message prediction
  - Implement batch prediction
  - Implement interactive input function
  - **Deliverable**: Complete `notebooks/03_prediction.ipynb`

- **Task 3.11**: Integration testing
  - Test end-to-end prediction flow
  - Test dengan berbagai input
  - Test error handling
  - **Deliverable**: Integration test report

- **Task 3.12**: Code review & refactoring
  - Review semua code
  - Refactor untuk readability
  - Add final documentation
  - **Deliverable**: Final polished code

- **Deadline**: Akhir Minggu 4

---

#### **Orang 4 - DevOps / QA** 🎯 LEAD

- **Task 4.10**: Comprehensive system testing
  - Test semua 3 notebooks end-to-end
  - Test pada berbagai system (macOS, Windows, Linux)
  - Test dengan different data sizes
  - **Deliverable**: System testing report

- **Task 4.11**: Final documentation
  - Update comprehensive README
  - Create quick start guide
  - Create troubleshooting guide
  - **Deliverable**: Complete documentation

- **Task 4.12**: Project release & cleanup
  - Final code review
  - Prepare for production
  - Create release notes
  - Cleanup & optimize repository
  - **Deliverable**: Release-ready project

- **Task 4.13**: Final project presentation
  - Create project summary
  - Prepare demo materials
  - Document lessons learned
  - **Deliverable**: Project presentation

- **Deadline**: Akhir Minggu 4 (Project Complete!)

---

## 🔄 Collaboration Points

| Minggu | Collaboration             | Pihak Terlibat    |
| ------ | ------------------------- | ----------------- |
| **W1** | Share environment setup   | All 4 orang       |
| **W1** | Review preprocessing code | Orang 2,3,4       |
| **W2** | Share cleaned dataset     | Orang 1 → Orang 2 |
| **W2** | Integrate preprocessing   | Orang 1,3         |
| **W3** | Model training support    | Orang 2,1,3       |
| **W3** | Integrate predictor       | Orang 2,3         |
| **W4** | End-to-end testing        | Orang 3,4         |
| **W4** | Final review & release    | All 4 orang       |

---

## 📦 Deliverables Per Minggu

### Minggu 1 Deliverables

```
✅ Development environment setup (all)
✅ data/dataset.csv (Orang 1)
✅ src/preprocessor.py dengan tests (Orang 3)
✅ Model research & architecture (Orang 2)
✅ Git workflow & QA plan (Orang 4)
```

### Minggu 2 Deliverables

```
✅ notebooks/01_eda.ipynb (Orang 1)
✅ data/dataset_clean.csv (Orang 1)
✅ Model training template ready (Orang 2)
✅ Preprocessing integration tested (Orang 3)
✅ Data validation report (Orang 4)
```

### Minggu 3 Deliverables

```
✅ notebooks/02_training.ipynb (Orang 2)
✅ 3 trained models (Orang 2)
✅ src/predictor.py dengan tests (Orang 3)
✅ Model performance report (Orang 4)
```

### Minggu 4 Deliverables

```
✅ notebooks/03_prediction.ipynb (Orang 3)
✅ Final documentation & README (Orang 4)
✅ System testing report (Orang 4)
✅ Project release ready ✨ (All)
```

---

## 📅 Weekly Standup Template

**Setiap akhir minggu, masing-masing orang report:**

```
## Minggu [N] Status Report

### Orang 1 - Data Engineer
- ✅ Completed: [tasks]
- 🔄 In Progress: [tasks]
- ⚠️  Blockers: [issues]
- 📅 Next Week: [plans]

### Orang 2 - ML Engineer
- ✅ Completed: [tasks]
- 🔄 In Progress: [tasks]
- ⚠️  Blockers: [issues]
- 📅 Next Week: [plans]

### Orang 3 - Backend Developer
- ✅ Completed: [tasks]
- 🔄 In Progress: [tasks]
- ⚠️  Blockers: [issues]
- 📅 Next Week: [plans]

### Orang 4 - DevOps / QA
- ✅ Completed: [tasks]
- 🔄 In Progress: [tasks]
- ⚠️  Blockers: [issues]
- 📅 Next Week: [plans]
```

---

## ⚠️ Key Assumptions & Dependencies

1. **Data Ready by End W1**: Orang 1 must deliver dataset untuk Orang 2
2. **Preprocessing Tested by End W1**: Orang 3 code harus ditest sebelum used di W2
3. **Cleaned Dataset by Mid W2**: Required untuk Orang 2 training di W3
4. **Model Ready by End W3**: Required untuk Orang 3 integration di W3
5. **Predictor Complete by Mid W4**: Required untuk Orang 4 final testing

---

## 🎯 Success Criteria

- ✅ Semua 3 notebooks complete & functional
- ✅ Model trained dengan accuracy > 90%
- ✅ All unit tests passing
- ✅ End-to-end prediction working
- ✅ Complete documentation
- ✅ Ready for production deployment
- ✅ All team members comfortable dengan codebase

---

## 📝 Notes

- **Meeting frequency**: 2-3x per minggu (standup + sync)
- **Git workflow**: Feature branches, code review sebelum merge ke main
- **Documentation**: Update incrementally, jangan di-defer hingga akhir
- **Communication**: Use GitHub Issues untuk blockers & collaboration
- **Flexibility**: Adjust task jika ada blocker, communicate early
