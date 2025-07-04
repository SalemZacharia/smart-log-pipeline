import pandas as pd
import re

def parse_log_file(file_path):
    pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(INFO|WARN|ERROR)\s+(.*)")
    logs = []

    with open(file_path, "r") as file:
        for line in file:
            match = pattern.match(line)
            if match:
                logs.append({
                    "timestamp": match.group(1),
                    "level": match.group(2),
                    "message": match.group(3)
                })

    return pd.DataFrame(logs)

# Test
if __name__ == "__main__":
    df = parse_log_file("data/sample.log")
    print(df.head())
