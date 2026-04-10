"""
File: src/predictor.py
Deskripsi: Modul prediksi spam/ham untuk pesan baru
"""

import joblib
import numpy as np
from pathlib import Path
from .preprocessor import preprocess


class SpamHamPredictor:
    """
    Kelas untuk melakukan prediksi spam/ham pada teks baru.
    
    Cara pakai:
        predictor = SpamHamPredictor()
        result = predictor.predict("Selamat Anda menang hadiah 1 juta rupiah!")
        print(result)
    """

    def __init__(self, model_path: str = 'models/spam_ham_model.pkl'):
        model_file = Path(model_path)
        if not model_file.exists():
            raise FileNotFoundError(
                f"Model tidak ditemukan di: {model_path}\n"
                "Jalankan notebook 02_training.ipynb terlebih dahulu."
            )
        self.model = joblib.load(model_path)
        self.classes = self.model.classes_

    def predict(self, text: str) -> dict:
        """
        Prediksi satu pesan.
        
        Parameter:
            text (str): Teks pesan yang akan diklasifikasi
            
        Return:
            dict dengan key:
                - teks_asli: teks input
                - teks_diproses: teks setelah preprocessing
                - prediksi: 'spam' atau 'ham'
                - probabilitas: dict {'spam': float, 'ham': float}
                - keyakinan: persentase keyakinan prediksi (%)
        """
        processed = preprocess(text)
        pred = self.model.predict([processed])[0]
        proba = self.model.predict_proba([processed])[0]
        
        proba_dict = {cls: round(float(p) * 100, 2) 
                      for cls, p in zip(self.classes, proba)}
        keyakinan = proba_dict[pred]
        
        return {
            'teks_asli': text,
            'teks_diproses': processed,
            'prediksi': pred,
            'probabilitas': proba_dict,
            'keyakinan': keyakinan,
        }

    def predict_batch(self, texts: list) -> list:
        """
        Prediksi banyak pesan sekaligus.
        
        Parameter:
            texts (list of str): Daftar teks pesan
            
        Return:
            list of dict (hasil predict() untuk setiap pesan)
        """
        return [self.predict(t) for t in texts]

    def display_result(self, result: dict) -> None:
        """
        Menampilkan hasil prediksi dengan format yang rapi.
        """
        label = result['prediksi'].upper()
        emoji = "🚫" if result['prediksi'] == 'spam' else "✅"
        
        print("=" * 55)
        print(f"  HASIL KLASIFIKASI PESAN")
        print("=" * 55)
        print(f"  Pesan   : {result['teks_asli'][:60]}{'...' if len(result['teks_asli']) > 60 else ''}")
        print(f"  Prediksi: {emoji}  {label}")
        print("-" * 55)
        print("  Probabilitas:")
        for cls, pct in result['probabilitas'].items():
            bar_len = int(pct / 2.5)
            bar = "█" * bar_len + "░" * (40 - bar_len)
            print(f"    {cls.upper():4s}  [{bar}] {pct:5.1f}%")
        print("=" * 55)
