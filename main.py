from ingestion import parse_logs
from transformation import transform_logs
from enrichment import enrich_logs
from export import export_logs

# Fichiers d'entrée/sortie
input_path = "./data/raw"
parsed_path = "./data/processed/parsed_logs.csv"
transformed_path = "./data/processed/transformed_logs.csv"

# Pipeline complet
parse_logs(input_path, parsed_path)
transform_logs(parsed_path, transformed_path)
enrich_logs(transformed_path)
export_logs(transformed_path)

print("✅ Pipeline complet terminé.")
