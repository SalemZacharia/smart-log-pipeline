import pandas as pd
from pathlib import Path

def export_logs(input_file):
    df = pd.read_csv(input_file)

  
    export_dir = Path("./data/exported")
    export_dir.mkdir(parents=True, exist_ok=True)

   
    csv_path = export_dir / "logs_export.csv"
    df.to_csv(csv_path, index=False)
    print(f"✅ CSV exporté vers {csv_path}")

    
    json_path = export_dir / "logs_export.json"
    df.to_json(json_path, orient="records", lines=True)
    print(f"✅ JSON exporté vers {json_path}")

    
    parquet_path = export_dir / "logs_export.parquet"
    df.to_parquet(parquet_path)
    print(f"✅ Parquet exporté vers {parquet_path}")

if __name__ == "__main__":
    input_path = "./data/processed/enriched_logs.csv"
    export_logs(input_path)
