import pandas as pd

def transform_logs(input_file, output_file):
    df = pd.read_csv(input_file)

   
    df['message_length'] = df['message'].apply(len)

    
    keywords = ['error', 'warn', 'fail', 'exception']
    for kw in keywords:
        df[f'has_{kw}'] = df['message'].str.lower().str.contains(kw)


    df['level'] = df['level'].str.upper()

    df.to_csv(output_file, index=False)
    print(f"✅ Transformed logs saved to {output_file}")

if __name__ == "__main__":
    input_path = "./data/processed/parsed_logs.csv"
    output_path = "./data/processed/transformed_logs.csv"
    transform_logs(input_path, output_path)
   
