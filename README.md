# Spam/Ham Classifier

Sistem klasifikasi pesan spam dan ham menggunakan Machine Learning.

## Cara Penggunaan

### 0. Clone Repository

```bash
git clone https://github.com/zhekabaila/spam-ham-classifier.git
cd spam-ham-classifier
```

### 1. Setup Virtual Environment

```bash
# Buat virtual environment
python3 -m venv venv

# Aktivasi virtual environment
# Pada macOS/Linux:
source venv/bin/activate

# Pada Windows:
# venv\Scripts\activate
```

Setelah diaktifkan, command prompt Anda akan menampilkan `(venv)` di awal:

```
(venv) user@machine spam-ham-classifier %
```

### 2. Install Dependensi

```bash
pip install -r requirements.txt
```

Proses instalasi akan memuat semua library yang diperlukan:

- pandas, numpy (data handling)
- scikit-learn (machine learning)
- matplotlib, seaborn (visualization)
- nltk (natural language processing)
- joblib (model serialization)
- jupyter (notebook environment)

### 3. Siapkan Dataset

Letakkan dataset CSV Anda di `data/dataset.csv` dengan kolom **wajib**:

- `kategori` → nilai: `spam` atau `ham`
- `pesan` → isi teks pesan

**Contoh format CSV:**

```
kategori,pesan
spam,Selamat Anda menang hadiah 1 juta rupiah!
ham,Hai, apa kabar? Besok kita jadi ketemuan?
```

### 4. Jalankan Notebook Secara Berurutan

```bash
# Mulai Jupyter server
jupyter notebook
```

Browser akan otomatis membuka `http://localhost:8888`

Jalankan notebooks dalam urutan ini:

1. **`notebooks/01_eda.ipynb`** — Exploratory Data Analysis
   - Load dan cleaning dataset
   - Analisis distribusi label dan panjang pesan
   - Preprocessing teks dan simpan dataset bersih

2. **`notebooks/02_training.ipynb`** — Training Model
   - Train 3 model: Naive Bayes, Logistic Regression, Linear SVM
   - Evaluasi dengan cross-validation
   - Pilih model terbaik dan simpan

3. **`notebooks/03_prediction.ipynb`** — Prediksi Pesan
   - Load model terlatih
   - Test prediksi single/batch messages
   - Interactive input untuk testing

### 5. Jalankan Streamlit Web App

Setelah model berhasil dilatih di notebook 02, Anda dapat menggunakan web interface interaktif dengan Streamlit.

#### Apa itu Streamlit?

Streamlit adalah framework Python yang memudahkan pembuatan web applications untuk machine learning tanpa perlu HTML/CSS/JavaScript. Cocok untuk:

- 🎨 Interactive visualizations
- 📊 Real-time predictions
- 🚀 Rapid prototyping
- 📱 Mobile responsive

#### Menjalankan Streamlit App

```bash
# Pastikan virtual environment sudah aktif
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Jalankan aplikasi Streamlit
streamlit run app.py
```

Aplikasi akan berjalan di: **http://localhost:8501**

Browser akan otomatis terbuka. Jika tidak, buka manual URL di atas.

**Untuk stop app**: Tekan `Ctrl+C` di terminal

#### Fitur Streamlit App

✅ **Single Message Prediction**

- Input satu pesan
- Visualisasi real-time dengan gauge chart
- Probability breakdown dengan bar chart
- Display pesan setelah preprocessing

✅ **Batch Prediction**

- Analisis multiple pesan sekaligus
- Hasil dalam format table
- Quick statistics

✅ **Example Buttons**

- Contoh pesan spam & ham
- Quick testing tanpa mengetik

✅ **Beautiful Dark Theme UI**

- Modern design dengan custom CSS
- Responsive pada mobile
- Easy to read visualizations

#### Cara Menggunakan App

**Step 1**: Masukkan pesan di textarea

```
Contoh: "Selamat Anda memenangkan hadiah 1 juta rupiah!"
```

**Step 2**: Klik tombol "Cek Pesan"

**Step 3**: Lihat hasil prediksi:

- 🚫 SPAM atau ✅ HAM
- Confidence percentage (0-100%)
- Gauge chart menunjukkan spam probability
- Bar chart breakdown
- Pesan yang sudah diproses

**Step 4 (Optional)**: Untuk batch prediction:

- Scroll ke section "Cek Banyak Pesan Sekaligus"
- Masukkan multiple pesan (satu per baris)
- Klik "Analisis Semua Pesan"
- Lihat hasil dalam table

#### Running Options

**Option 1: Development Mode** (untuk editing code)

```bash
streamlit run app.py
# Auto-reload saat file berubah
```

**Option 2: Custom Port**

```bash
streamlit run app.py --server.port 8080
```

**Option 3: Docker** (untuk deployment)

```bash
docker build -t spam-classifier .
docker run -p 8501:8501 spam-classifier
```

**Option 4: Streamlit Cloud** (free hosting)

1. Push code ke GitHub
2. Kunjungi https://streamlit.io/cloud
3. Connect repository Anda
4. Deploy dalam 1 klik!

#### Requirements untuk Streamlit

Pastikan dependensi berikut sudah terinstall (seharusnya sudah ada di `requirements.txt`):

```
streamlit>=1.28.0
plotly>=5.13.0
scikit-learn>=1.3.0
nltk>=3.8.0
joblib>=1.3.0
pandas>=1.5.0
numpy>=1.24.0
```

#### Troubleshooting Streamlit

**Problem**: App tidak terbuka di browser

- **Solusi**: Buka manual http://localhost:8501

**Problem**: Model tidak ditemukan

- **Solusi**: Pastikan sudah menjalankan `02_training.ipynb` terlebih dahulu. Model harus ada di `models/spam_ham_model.pkl`

**Problem**: NLTK stopwords error

- **Solusi**: Cell pertama dari `01_eda.ipynb` sudah download NLTK resources. Jika masih error, manual run:

```python
import nltk
nltk.download('stopwords')
```

**Problem**: Styling tidak terlihat dengan benar

- **Solusi**: Hard refresh browser (Ctrl+Shift+R) atau clear cache browser

#### Tips & Tricks

🎯 **Quick Testing**: Gunakan example buttons untuk test spam vs ham dengan cepat

📊 **Batch Analysis**: Bagus untuk testing multiple messages dari Excel/CSV

💾 **Model Caching**: App auto-cache model setelah load pertama (very fast untuk prediksi berikutnya)

📱 **Mobile**: App responsive, bisa dibuka dari smartphone

🌐 **Share**: Jika deploy ke Streamlit Cloud, bisa share URL ke teman/kolega

### 6. Contoh Penggunaan via Python

Setelah model berhasil dilatih, gunakan sebagai berikut:

```python
from src.predictor import SpamHamPredictor

# Load model
predictor = SpamHamPredictor(model_path='models/spam_ham_model.pkl')

# Single prediction
hasil = predictor.predict("Selamat Anda menang hadiah 1 juta!")
predictor.display_result(hasil)

# Batch predictions
pesan_list = ["pesan1", "pesan2", "pesan3"]
hasil_batch = predictor.predict_batch(pesan_list)
```

### 6. Deaktifasi Virtual Environment

Setelah selesai kerja:

```bash
deactivate
```

## Struktur Folder

```
spam-ham-classifier/
├── venv/                    # Virtual environment (auto-generated)
├── data/
│   └── dataset.csv          # letakkan dataset di sini
├── models/
│   └── (model tersimpan di sini)
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_training.ipynb
│   └── 03_prediction.ipynb
├── src/
│   ├── __init__.py
│   ├── preprocessor.py
│   └── predictor.py
├── .gitignore               # Git ignore rules
├── requirements.txt
├── README.md
└── .instructions.md         # Project specifications
```

## Troubleshooting

### `ModuleNotFoundError` saat import library

**Solusi**: Pastikan virtual environment telah diaktifkan dengan benar.

```bash
# Cek apakah venv aktif (harus ada (venv) di prompt)
source venv/bin/activate
# Kemudian install lagi
pip install -r requirements.txt
```

### Notebook tidak menemukan module `src`

**Solusi**: Pastikan menjalankan notebook dari folder project root. Cell pertama harus berisi:

```python
import sys
sys.path.append('../')
```

### NLTK stopwords error

**Solusi**: Jalankan cell pertama dari `01_eda.ipynb` terlebih dahulu, yang akan download resource NLTK otomatis.

### Model file not found saat menjalankan `03_prediction.ipynb`

**Solusi**: Pastikan telah menjalankan `02_training.ipynb` terlebih dahulu hingga model berhasil disimpan.

---

## Catatan Penting

- **Nama kolom dataset** harus `kategori` dan `pesan`. Jika berbeda, sesuaikan saat load data.
- **Bahasa dataset**: Preprocessing dikonfigurasi untuk **bahasa Indonesia**. Jika dataset bahasa Inggris, ubah parameter `language='english'` di `preprocessor.py`.
- **Urutan eksekusi notebook**: 01 → 02 → 03. Jangan lewati urutan ini.
- **Model yang dibandingkan**: Naive Bayes, Logistic Regression, dan Linear SVM. Model terbaik dipilih otomatis berdasarkan F1 Score cross-validation.
- **Output model**: Tersimpan di folder `models/` setelah notebook 02 selesai dijalankan.
