"""
File: src/preprocessor.py
Deskripsi: Modul preprocessing teks untuk klasifikasi spam/ham
"""

import re
import string
import nltk
from nltk.corpus import stopwords

# Download resource NLTK yang dibutuhkan
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

def clean_text(text: str) -> str:
    """
    Membersihkan teks mentah:
    - Lowercase
    - Hapus URL
    - Hapus angka
    - Hapus tanda baca
    - Hapus whitespace berlebih
    """
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)         # hapus URL
    text = re.sub(r'\d+', '', text)                     # hapus angka
    text = text.translate(str.maketrans('', '', string.punctuation))  # hapus tanda baca
    text = re.sub(r'\s+', ' ', text).strip()            # normalisasi spasi
    return text


def remove_stopwords(text: str, language: str = 'indonesian') -> str:
    """
    Menghapus stopwords dari teks.
    Gunakan language='english' jika dataset berbahasa Inggris.
    """
    try:
        stop_words = set(stopwords.words(language))
    except OSError:
        stop_words = set(stopwords.words('english'))
    
    tokens = text.split()
    filtered = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered)


def preprocess(text: str, remove_stop: bool = True) -> str:
    """
    Pipeline preprocessing lengkap:
    1. clean_text
    2. remove_stopwords (opsional)
    """
    text = clean_text(text)
    if remove_stop:
        text = remove_stopwords(text)
    return text
