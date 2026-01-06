# Experiment Tracking: The Truth Ledger

## 1. Tracking Philosophy
In a multi-model platform, we don't just log results; we log the **Provenance** (Source) of every prediction. This allows us to answer: *Which model version, with which data, produced this specific output?*

## 2. The Tracking Contract (Agnosticism)
The system is designed to interface with any tracking provider (Reference: **MLflow**), but the code remains generic. It must capture:
- **Parameters:** Hyperparameters (e.g., `learning_rate`, `max_depth`).
- **Metrics:** Performance indicators (e.g., `RMSE`, `MAE`, `R2 Score`).
- **Artifacts:** The serialized model file, feature importance plots, and the `uv.lock` file for reproducibility.
- **Tags:** Task type (e.g., `duration_prediction`), environment (`staging`/`prod`), and data version.

## 3. Automated Lineage
Every time a model is trained or run in a pipeline:
1. **Auto-Logging:** The Adapter automatically pushes metrics to the central server.
2. **Commit Hash:** The current Git commit and Python version are recorded to ensure the code matches the model.
3. **Data Hash:** A signature of the training data (from Polars) is saved to detect "Data Drift".

## 4. Model Registry Integration
The "Registry" acts as the bridge between development and production:
- **Promotion Logic:** Models move from `Candidate` to `Champion` based on predefined metric thresholds.
- **Rollback:** If a new `Duration` model performs poorly in production, the Registry allows an instant fallback to the previous version without code changes.

## 5. Performance Monitoring
Post-deployment, we track the **Residuals** (Difference between prediction and reality). This data feeds back into the next training cycle, creating a "Self-Improving Loop".