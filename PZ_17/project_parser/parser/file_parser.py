import re
from pathlib import Path
from parser.regex_patterns import PATTERNS


def parse_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    result = {}
    for key, pattern in PATTERNS.items():
        match = re.search(pattern, text)
        result[key] = match.group(1).strip() if match else None

    return result


def parse_all_texts(input_folder):
    folder = Path(input_folder)
    parsed = []
    for file in folder.glob("*.txt"):
        parsed.append(parse_text_file(file))
    return parsed
