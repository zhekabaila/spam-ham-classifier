# Daftar Tugas - Spam/Ham Classifier

**Tim**: 4 orang  
**Durasi**: 4 minggu  
**Catatan**: Semua development di lokal dulu, migrasi ke Google Colab di minggu 4

---

## 📅 MINGGU 1: Setup & Persiapan Data

### Orang 1 - Data Engineer

| Tugas                  | Status | Keterangan                                                     |
| ---------------------- | ------ | -------------------------------------------------------------- |
| Cari & siapkan dataset | ⬜     | Cari minimal 1000 pesan (spam & ham), simpan dalam CSV         |
| Load & cek awal        | ⬜     | Buka dataset, cek ukuran, tipe data, missing values            |
| Setup folder data      | ⬜     | Buat folder `data/` dan `notebooks/`, letakkan dataset di sini |

### Orang 2 - ML Engineer

| Tugas                 | Status | Keterangan                                                           |
| --------------------- | ------ | -------------------------------------------------------------------- |
| Rencana model         | ⬜     | Tulis 3 model: Naive Bayes, Logistic Regression, SVM                 |
| Setup environment     | ⬜     | Install Python, buat virtual env, install pandas, scikit-learn, nltk |
| Config hyperparameter | ⬜     | Tulis TF-IDF setting (max_features=10000, ngram 1-2)                 |

### Orang 3 - Developer

| Tugas             | Status | Keterangan                                                                 |
| ----------------- | ------ | -------------------------------------------------------------------------- |
| Struktur folder   | ⬜     | Buat folder: `src/`, `notebooks/`, `models/`, `config/`                    |
| File preprocessor | ⬜     | Buat `src/preprocessor.py`: clean_text(), remove_stopwords(), preprocess() |
| Test preprocessor | ⬜     | Test fungsi dengan sample pesan, pastikan jalan lancar                     |

### Orang 4 - QA

| Tugas                    | Status | Keterangan                                                |
| ------------------------ | ------ | --------------------------------------------------------- |
| Setup GitHub             | ⬜     | Buat repo, setup `.gitignore`, buat struktur awal         |
| Cek environment semua    | ⬜     | Pastikan semua anggota punya Python & bisa pull dari repo |
| Verifikasi code minggu 1 | ⬜     | Test data ada, folder lengkap, code tidak error           |

---

## 📅 MINGGU 2: Eksplorasi Data & Persiapan Training

### Orang 1 - Data Engineer

| Tugas             | Status | Keterangan                                                    |
| ----------------- | ------ | ------------------------------------------------------------- |
| Buat EDA notebook | ⬜     | Lihat distribusi spam/ham, length pesan, missing values       |
| Bersihkan data    | ⬜     | Hapus null, duplikat, pesan kosong → simpan dataset_clean.csv |
| Analisis kualitas | ⬜     | Tulis laporan singkat tentang kondisi data                    |

### Orang 2 - ML Engineer

| Tugas              | Status | Keterangan                                            |
| ------------------ | ------ | ----------------------------------------------------- |
| Design TF-IDF      | ⬜     | Setup vectorizer dengan parameter dari config         |
| Persiapkan 3 model | ⬜     | Buat pipeline untuk 3 model, siapkan train-test split |
| Setup metric       | ⬜     | Siapkan cara hitung accuracy, precision, recall, F1   |

### Orang 3 - Developer

| Tugas                  | Status | Keterangan                                       |
| ---------------------- | ------ | ------------------------------------------------ |
| Lengkapi preprocessor  | ⬜     | Tambah docstring & error handling                |
| Buat utility functions | ⬜     | Fungsi load_data(), save_model(), load_model()   |
| Test integration       | ⬜     | Test preprocessor bisa dipakai di EDA & training |

### Orang 4 - QA

| Tugas                  | Status | Keterangan                                          |
| ---------------------- | ------ | --------------------------------------------------- |
| Verifikasi data        | ⬜     | Cek format dataset_clean.csv benar, cek sample rows |
| Test code minggu 1 & 2 | ⬜     | Run preprocessor, cek tidak error                   |
| Update dokumentasi     | ⬜     | Update README dengan progress minggu 1 & 2          |

---

## 📅 MINGGU 3: Training & Evaluasi Model

### Orang 1 - Data Engineer

| Tugas                 | Status | Keterangan                                             |
| --------------------- | ------ | ------------------------------------------------------ |
| Prepare training data | ⬜     | Bagi data 80% training, 20% testing (stratified split) |
| Monitor quality       | ⬜     | Cek gak ada data leakage, distribusi label benar       |
| Support ML Engineer   | ⬜     | Bantu kalau ada issue dengan data saat training        |

### Orang 2 - ML Engineer

| Tugas            | Status | Keterangan                                                      |
| ---------------- | ------ | --------------------------------------------------------------- |
| Train 3 model    | ⬜     | Train NB, LogReg, SVM dengan training data                      |
| Evaluasi model   | ⬜     | Hitung F1 score, accuracy, precision, recall (cross-validation) |
| Pilih best model | ⬜     | Pilih model terbaik, save ke models/spam_ham_model.pkl          |

### Orang 3 - Developer

| Tugas            | Status | Keterangan                                             |
| ---------------- | ------ | ------------------------------------------------------ |
| Class Predictor  | ⬜     | Buat SpamHamPredictor class untuk load model & predict |
| Test predictor   | ⬜     | Test single message, batch messages, cek output benar  |
| Handle edge case | ⬜     | Handle empty input, special chars, panjang ekstrim     |

### Orang 4 - QA

| Tugas            | Status | Keterangan                                          |
| ---------------- | ------ | --------------------------------------------------- |
| Test model       | ⬜     | Load model, cek bisa predict, test probability      |
| Verifikasi hasil | ⬜     | Cek metric reasonable (accuracy > 85%), gak overfit |
| Test predictor   | ⬜     | Run predictor class, test single & batch prediction |

---

## 📅 MINGGU 4: Testing, Polish & Migrasi Colab

### Orang 1 - Data Engineer

| Tugas                | Status | Keterangan                                             |
| -------------------- | ------ | ------------------------------------------------------ |
| Siapkan test dataset | ⬜     | Buat 20-30 test messages (spam & ham) untuk final test |
| Final validation     | ⬜     | Cek semua dataset, verify gak ada data leakage         |
| Prepare Colab        | ⬜     | Upload dataset ke Google Drive untuk Colab             |

### Orang 2 - ML Engineer

| Tugas              | Status | Keterangan                                              |
| ------------------ | ------ | ------------------------------------------------------- |
| Dokumentasi model  | ⬜     | Tulis hyperparameter, training process, hasil accuracy  |
| Polish notebook    | ⬜     | Rapikan training notebook, tambah comment & visualisasi |
| Export untuk Colab | ⬜     | Format model biar bisa di-load di Colab                 |

### Orang 3 - Developer

| Tugas               | Status | Keterangan                                                 |
| ------------------- | ------ | ---------------------------------------------------------- |
| Prediction notebook | ⬜     | Buat notebook untuk demo prediction                        |
| Test end-to-end     | ⬜     | Test workflow lengkap: load → preprocess → train → predict |
| Setup untuk Colab   | ⬜     | Siapkan code biar bisa run di Colab (handle Drive mount)   |

### Orang 4 - QA

| Tugas             | Status | Keterangan                                             |
| ----------------- | ------ | ------------------------------------------------------ |
| System testing    | ⬜     | Test seluruh workflow dari awal sampai akhir           |
| Final dokumentasi | ⬜     | Update README lengkap, tulis tutorial, troubleshooting |
| Test di Colab     | ⬜     | Migrasi ke Colab, test code berjalan di Colab          |

---

## 📊 Ringkasan Per Minggu

| Minggu | Fokus                | Deliverable                                                        |
| ------ | -------------------- | ------------------------------------------------------------------ |
| 1      | Setup & Persiapan    | Environment siap, struktur folder, dataset ada, preprocessor jalan |
| 2      | EDA & Cleaning       | Data bersih, visualisasi, persiapan untuk training                 |
| 3      | Training & Selection | 3 model trained, best model selected & saved                       |
| 4      | Testing & Colab      | End-to-end testing, dokumentasi lengkap, ready untuk Colab         |

---

## ✅ Penting

- **QA hanya testing**: Tidak setup project, hanya verifikasi & test
- **Local development dulu**: Semua di lokal sampai minggu 4
- **Colab di akhir**: Minggu 4 untuk final testing & demo
- **Commit regular**: Push ke GitHub setiap minggu
- **Update progress**: Komunikasi harian tentang progress
