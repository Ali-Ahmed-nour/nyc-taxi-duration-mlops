import os
from pathlib import Path
from datetime import datetime
from typing import TypedDict


# English comments only
class ProjectConfig(TypedDict):
    taxi_type: str
    year: int
    month: int
    # Cloud paths
    bucket_name: str
    gcs_raw_path: str
    gcs_processed_path: str
    # Local paths for cache
    raw_path: str
    processed_path: str
    model_path: str
    # Features from your notebook
    categorical_features: list[str]
    numerical_features: list[str]
    target: str
    model_type: str


def get_config(
    taxi_type="yellow", year=2024, month=1, model_type="xgb"
) -> ProjectConfig:
    # Set your bucket name here
    bucket_name = os.getenv("GCP_BUCKET_NAME", "nyc-taxi-duration-ali")

    # Base directory logic
    base_dir = Path(__file__).resolve().parent.parent
    data_file = f"{taxi_type}_tripdata_{year:04d}-{month:02d}.parquet"

    # Versioning for models
    today = datetime.now().strftime("%Y-%m-%d")
    model_name = f"model_{model_type}_{taxi_type}_{year:04d}-{month:02d}_v_{today}.bin"

    config: ProjectConfig = {
        "taxi_type": taxi_type,
        "year": year,
        "month": month,
        "model_type": model_type,
        "bucket_name": bucket_name,
        # GCS Paths
        "gcs_raw_path": f"gs://{bucket_name}/raw/{data_file}",
        "gcs_processed_path": f"gs://{bucket_name}/processed/{data_file}",
        # Local Paths (Corrected for the new structure)
        "raw_path": str(base_dir / "data" / "raw" / data_file),
        "processed_path": str(base_dir / "data" / "processed" / data_file),
        "model_path": str(base_dir / "models" / model_name),
        "categorical_features": ["PULocationID", "DOLocationID"],
        "numerical_features": ["trip_distance"],
        "target": "duration",
    }
    return config
