import json

with open("Dataset/train.jsonl", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        try:
            json.loads(line)
        except json.JSONDecodeError as e:
            print(f"Line {i} is invalid: {e}")
