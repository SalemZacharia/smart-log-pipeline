import pandas as pd

def enrich_logs(input_file, output_file):
    df = pd.read_csv(input_file)

    
    def compute_severity(row):
        if row['has_error'] or row['has_exception']:
            return 'High'
        elif row['has_warn']:
            return 'Medium'
        else:
            return 'Low'

    df['severity'] = df.apply(compute_severity, axis=1)

   
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    df['daytime'] = df['hour'].apply(lambda h: 'Night' if h < 6 or h > 22 else ('Evening' if h > 17 else 'Day'))


    df.to_csv(output_file, index=False)
    print(f"✅ Enriched logs saved to {output_file}")

if __name__ == "__main__":
    input_path = "./data/processed/transformed_logs.csv"
    output_path = "./data/processed/enriched_logs.csv"
    enrich_logs(input_path, output_path)
