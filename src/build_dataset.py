# build_dataset.py
import json
import os

INPUT_JSON = "../dataset/proses/parsed_data.json"
OUTPUT_JSONL = "../dataset/proses/dataset.jsonl"


def build_jsonl():
    # 1. Baca hasil parsing PDF
    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_records = 0

    # 2. Tulis ke format JSONL
    with open(OUTPUT_JSONL, "w", encoding="utf-8") as out:
        for item in data:
            label = item["label"]

            ordered_text = []

            # 3. JAGA URUTAN HALAMAN
            for page in item["pages"]:
                # teks dulu
                if page["text"].strip():
                    ordered_text.append(page["text"].strip())

                # lalu gambar → TOKEN SAJA (TANPA BASE64)
                for _ in page["images"]:
                    ordered_text.append("<image>")

            final_text = "\n".join(ordered_text)

            record = {
                "text": final_text,
                "label": label
            }

            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            total_records += 1

    print("✅ build_dataset.py selesai")
    print(f"📄 Total data: {total_records}")
    print(f"📁 Output: {OUTPUT_JSONL}")


if __name__ == "__main__":
    build_jsonl()
