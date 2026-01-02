from transformers import (
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
from datasets import load_from_disk
import os

os.environ["TRANSFORMERS_NO_SAFE_TENSORS"] = "1"

MODEL_NAME = "prajjwal1/bert-tiny"
TOKENIZED_PATH = "../dataset/proses/tokenized"
OUTPUT_DIR = "../model"

dataset = load_from_disk(TOKENIZED_PATH)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=2,
    use_safetensors=False
)

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=1,
    num_train_epochs=10,
    learning_rate=5e-5,
    logging_steps=1,
    save_strategy="no",
    report_to="none",
    dataloader_pin_memory=False
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

trainer.train()

model.save_pretrained(OUTPUT_DIR)
print("✅ Training selesai (bert-tiny)")
