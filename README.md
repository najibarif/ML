# Proposal Classification (Lolos / Tidak Lolos)

Model NLP untuk mengklasifikasikan proposal berdasarkan isi teks dan gambar.

## Pipeline
1. PDF → Text + Embedded Image Tokens
2. Dataset JSONL
3. Tokenization
4. Training (BERT Tiny)
5. Inference Proposal Baru

## Cara Menjalankan
```bash
pip install -r requirements.txt
python src/train.py
python src/predict.py
