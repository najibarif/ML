# 📄 Klasifikasi Proposal dengan NLP

Sistem untuk mengklasifikasikan proposal menjadi Lolos/Tidak Lolos menggunakan NLP dan Machine Learning.

## � Penjelasan Langkah-langkah

1. **Ekstrak Teks dari PDF** (`pdf_parser.py`)
   - Membaca file PDF dari folder `dataset/raw/`
   - Mengekstrak teks dari setiap halaman
   - Menyimpan teks hasil ekstraksi ke folder `dataset/proses/`

2. **Membangun Dataset** (`build_dataset.py`)
   - Menggabungkan teks dari semua file
   - Memberi label otomatis berdasarkan folder asal (lolos/tidak_lolos)
   - Menyimpan dalam format JSONL yang rapi

3. **Tokenisasi** (`tokenize_dataset.py`)
   - Memotong teks menjadi token (kata/kalimat)
   - Mengubah teks menjadi angka (numerical)
   - Menambahkan padding/truncate ke 512 token
   - Membagi data menjadi training & testing

4. **Training Model** (`train.py`)
   - Membangun arsitektur model
   - Melatih model dengan data training
   - Mengevaluasi performa dengan data testing
   - Menyimpan model terlatih ke folder `model/`

5. **Prediksi** (`predict.py`)
   - Menerima input file PDF baru
   - Melakukan preprocessing yang sama
   - Memprediksi kelas (Lolos/Tidak Lolos)
   - Menampilkan hasil prediksi dan confidence score

## �🚀 Cara Menggunakan

### 1. Persiapan
```bash
# Buat virtual environment
python -m venv venv
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 2. Struktur Folder
Buat folder dan letakkan file PDF proposal:
```
ML/
├── dataset/
│   ├── raw/
│   │   ├── lolos/       # PDF yang lolos
│   │   └── tidak_lolos/ # PDF yang tidak lolos
│   └── proses/          # Hasil pemrosesan
└── data/
    └── uji/            # PDF untuk prediksi
```

### 3. Proses Utama

1. **Ekstrak Teks** dari PDF:
   ```bash
   python src/pdf_parser.py
   ```

2. **Buat Dataset**:
   ```bash
   python src/build_dataset.py
   ```

3. **Tokenisasi**:
   ```bash
   python src/tokenize_dataset.py
   ```

4. **Training**:
   ```bash
   python src/train.py
   ```

5. **Prediksi**:
   ```bash
   python src/predict.py --input data/uji/proposal_anda.pdf
   ```

## 📋 Hasil yang Diharapkan
- **Model** disimpan di folder `model/`
- **Laporan evaluasi** di terminal yang menampilkan:
  - Akurasi model
  - Loss
  - Metrik evaluasi lainnya

## 🛠️ Teknologi yang Digunakan
- **Bahasa Pemrograman**: Python 3.9+
- **Machine Learning**: PyTorch/TensorFlow
- **NLP**: Transformers (Hugging Face)
- **PDF Processing**: PyMuPDF
- **Data Processing**: Pandas, NumPy

## ⚠️ Catatan Penting
1. **Persyaratan File**
   - File PDF tidak boleh terproteksi
   - Format teks harus terbaca (bukan hasil scan)

2. **Data Training**
   - Minimal 10 contoh per kelas
   - Semakin banyak data, semakin baik hasilnya

3. **Keterbatasan**
   - Maksimal 512 token per dokumen
   - Performa tergantung kualitas data training
   - Waktu training bisa lama untuk dataset besar

---
**🔄 Versi**: 1.0.0  
**📅 Update Terakhir**: Januari 2025
