from transformers import AutoTokenizer
from datasets import load_dataset
import os

MODEL_NAME = "prajjwal1/bert-tiny"
DATASET_PATH = "../dataset/proses/dataset.jsonl"
OUTPUT_DIR = "../dataset/proses/tokenized"
MAX_LEN = 512

os.makedirs(OUTPUT_DIR, exist_ok=True)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def tokenize_fn(batch):
    tokens = tokenizer(
        batch["text"],                 
        truncation=True,
        padding="max_length",
        max_length=MAX_LEN,
        return_attention_mask=True
    )
    tokens["labels"] = batch["label"]
    return tokens

dataset = load_dataset(
    "json",
    data_files=DATASET_PATH,
    split="train"
)

tokenized = dataset.map(
    tokenize_fn,
    batched=True,                     
    remove_columns=dataset.column_names,
    load_from_cache_file=False
)

tokenized.save_to_disk(OUTPUT_DIR)

print("✅ Tokenisasi selesai (DistilBERT-safe, 512 token)")
