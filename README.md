\# Proposal Classification System

Klasifikasi Proposal Lolos / Tidak Lolos Menggunakan NLP (Transformer)

\## 📌 Deskripsi

Repository ini berisi sistem \*\*machine learning berbasis Natural Language Processing (NLP)\*\* untuk mengklasifikasikan dokumen proposal (PDF) ke dalam dua kelas:

\- \*\*Lolos\*\*

\- \*\*Tidak Lolos\*\*

Sistem menggunakan pendekatan \*\*fine-tuning Transformer (DistilBERT / BERT-Tiny)\*\* dan dirancang untuk kebutuhan \*\*penelitian akademik / skripsi\*\*.

Alur kerja sistem:

PDF Proposal → Parsing Teks → Dataset → Tokenisasi → Training → Prediksi

\---

\## 🧱 Struktur Folder

project-root/

│

├── src/

│ ├── pdf\_parser.py # Parsing PDF → teks terurut

│ ├── build\_dataset.py # Membangun dataset JSONL

│ ├── tokenize\_dataset.py # Tokenisasi dataset

│ ├── train.py # Training model

│ └── predict.py # Prediksi proposal baru

│

├── dataset/

│ ├── raw/

│ │ ├── lolos/ # PDF proposal lolos

│ │ └── tidak\_lolos/ # PDF proposal tidak lolos

│ └── proses/ # Dataset hasil parsing & tokenisasi

│

├── data/

│ └── uji/

│ └── proposal\_baru.pdf # Contoh proposal untuk prediksi

│

├── models/ # Model hasil training (tidak di-commit)

├── requirements.txt

└── README.md


\---

\## ⚙️ Persyaratan Sistem

\- Python \*\*3.9 – 3.10\*\*

\- RAM minimal \*\*8 GB\*\* (CPU training)

\- OS: Windows / Linux / macOS

\> ⚠️ Training dilakukan \*\*CPU-only\*\* untuk menjaga kompatibilitas perangkat.

\---

\## 📦 Instalasi

Disarankan menggunakan virtual environment.


pip install -r requirements.txt

🚀 Cara Menjalankan (Dari Awal)

1️⃣ Siapkan Dataset PDF

Masukkan proposal ke folder berikut:

dataset/raw/lolos/

dataset/raw/tidak\_lolos/

2️⃣ Parsing PDF → Teks

python src/pdf\_parser.py

Output akan disimpan di:

dataset/proses/

3️⃣ Build Dataset JSONL

python src/build\_dataset.py

Menghasilkan file:

dataset/proses/dataset.jsonl

4️⃣ Tokenisasi Dataset

python src/tokenize\_dataset.py

Tokenisasi disesuaikan dengan batas 512 token (DistilBERT-safe).

5️⃣ Training Model

python src/train.py

Model hasil training akan disimpan di:

models/

6️⃣ Prediksi Proposal Baru

Letakkan file PDF uji di:

data/uji/proposal\_baru.pdf

Jalankan:

python src/predict.py

Output:

Prediksi kelas: Lolos / Tidak Lolos

Confidence score

🔁 Menjalankan Tanpa Training Ulang

Jika folder models/ sudah berisi model terlatih:

python src/predict.py

Parsing, tokenisasi, dan training tidak perlu diulang.

❌ File yang Tidak Di-Commit ke GitHub

File berikut tidak disarankan masuk repository:

dataset/

models/

File PDF proposal asli

Tambahkan ke .gitignore:

dataset/

models/

data/uji/

🧪 Model & Library

Transformer: DistilBERT / BERT-Tiny

Framework: Hugging Face Transformers

Dataset handling: datasets

PDF parsing: PyMuPDF

📚 Konteks Akademik

Sistem ini dikembangkan untuk penelitian/skripsi dengan topik:

Klasifikasi Proposal Berbasis Dokumen PDF Menggunakan Transformer dan NLP.

👤 Author

Naufal Najib

Informatics / Machine Learning Research

📄 Lisensi

Digunakan untuk keperluan pendidikan dan penelitian.
