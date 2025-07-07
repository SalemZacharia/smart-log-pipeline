import os
import csv
from datetime import datetime

class LogIngestor:
    def __init__(self, input_folder, output_file):
        self.input_folder = input_folder
        self.output_file = output_file

    def parse_line(self, line):
        
        try:
            parts = line.strip().split(' ', 2)
            timestamp_str = parts[0] + ' ' + parts[1]
            level = parts[2].split(' ')[0]
            message = parts[2][len(level):].strip()
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            return timestamp, level, message
        except Exception as e:
            print(f"[WARN] Failed to parse line: {line.strip()} ({e})")
            return None

    def process_files(self):
        with open(self.output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['timestamp', 'level', 'message'])

            for filename in os.listdir(self.input_folder):
                if filename.endswith(".log"):
                    file_path = os.path.join(self.input_folder, filename)
                    print(f"[INFO] Processing file: {file_path}")
                    with open(file_path, 'r') as file:
                        for line in file:
                            parsed = self.parse_line(line)
                            if parsed:
                                writer.writerow(parsed)

if __name__ == "__main__":
    input_folder = "./data/raw"
    output_file = "./data/processed/parsed_logs.csv"

    os.makedirs("./data/processed", exist_ok=True)

    ingestor = LogIngestor(input_folder, output_file)
    ingestor.process_files()

    print(f"[INFO] Logs parsed and saved to {output_file}")
