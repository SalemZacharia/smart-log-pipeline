from ingestion import parse_logs
from transformation import transform_logs
from enrichment import enrich_logs
from export import export_logs

if __name__ == "__main__":
    input_path = "./data/raw"
    parsed_path = "./data/processed/parsed_logs.csv"
    transformed_path = "./data/processed/transformed_logs.csv"
    enriched_path = "./data/processed/enriched_logs.csv"

    parse_logs(input_path, parsed_path)

    transform_logs(parsed_path, transformed_path)

    enrich_logs(transformed_path, enriched_path)

    export_logs(enriched_path)

    print("✅ Pipeline complete!")
