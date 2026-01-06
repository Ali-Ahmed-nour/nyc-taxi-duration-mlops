# Standardized Error Taxonomy: The Alert System

## 1. Error Governance
To maintain a scalable platform, generic exceptions (like `Exception` or `ValueError`) are strictly forbidden in the Core. Every failure must return a **Sovereign Error Code**.

## 2. Code Anatomy: `ERR_[LAYER]_[TYPE]_[SEQ]`
- **LAYER:** `DOM` (Domain), `INF` (Infrastructure), `APP` (Application).
- **TYPE:** `VAL` (Validation), `SYS` (System/IO), `ML` (Machine Learning).

## 3. The Central Error Registry

### A. Domain & Validation (The Guard)
| Code | Category | Description |
| :--- | :--- | :--- |
| `ERR_DOM_VAL_001` | Universal | Critical: Negative distance or invalid coordinates. |
| `ERR_DOM_VAL_002` | Universal | Critical: Temporal reversal (Dropoff before Pickup). |
| `ERR_DOM_TASK_101` | Task-Specific | Warning: Outlier detected for Duration model (Record skipped). |

### B. Infrastructure & Data (The Engine)
| Code | Category | Description |
| :--- | :--- | :--- |
| `ERR_INF_POL_001` | Data Ingestion | Polars failed to scan Parquet (Schema mismatch or corruption). |
| `ERR_INF_ML_002` | ML Registry | Model artifact not found in the registry (MLflow/Local). |

## 4. Handling & Resilience Policy
1. **Graceful Degradation:** If a model-specific error (`TASK_101`) occurs, the platform must continue processing other models for the same trip rather than failing the entire batch.
2. **Contextual Logging:** Every error must be logged with the `trip_id` and the `model_version` to facilitate instant debugging.
3. **Monitoring:** These codes are pushed to our tracking dashboard to monitor the "Health Rate" of our data streams.