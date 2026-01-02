import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from pdf_parser import pdf_to_ordered_text

MODEL_DIR = "../model"
PDF_PATH = "../dataset/uji/proposal_baru.pdf"

tokenizer = AutoTokenizer.from_pretrained("prajjwal1/bert-tiny")
model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
model.eval()

text = pdf_to_ordered_text(PDF_PATH)

inputs = tokenizer(
    text[:8000],
    truncation=True,
    padding="max_length",
    max_length=512,
    return_tensors="pt"
)

with torch.no_grad():
    outputs = model(**inputs)

pred = torch.argmax(outputs.logits, dim=1).item()

label = "LOLOS" if pred == 1 else "TIDAK LOLOS"
print("📄 Hasil Prediksi:", label)
