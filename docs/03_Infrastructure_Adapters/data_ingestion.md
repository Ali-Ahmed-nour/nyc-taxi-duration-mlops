# Data Ingestion: High-Performance Processing with Polars

## 1. The Streaming Mindset
To ensure the platform can scale from megabytes to terabytes of taxi data, we adopt a **Zero-Eager Policy**. Data is never loaded into RAM fully; it is streamed and filtered at the engine level.

## 2. Lazy Ingestion Pipeline
We utilize the `Polars.scan_parquet()` API to build a logical plan before execution:
1.  **Projection Pushdown:** Only the 20+ required columns are read from the disk.
2.  **Predicate Pushdown:** Universal invariants (e.g., Distance > 0) are filtered during the scan, not after.
3.  **Type Casting:** Enforcing strict types (e.g., casting IDs to String) to match the Domain Entity.

## 3. Feature Engineering at Scale
The ingestion adapter is responsible for "Materializing" features that models need:
-   **Temporal Extraction:** Deriving `hour`, `day_of_week`, and `is_weekend` from raw timestamps.
-   **Spatial Mapping:** Mapping Location IDs to normalized coordinates if required.

## 4. Performance Benchmarks (Target 2026)
- **Memory Efficiency:** Use of `collect(streaming=True)` for datasets exceeding available RAM.
- **Speed:** Leveraging Rust-backed multi-threading to process NYC Parquet files 10x faster than traditional Pandas.

## 5. From DataFrame to Domain
Once filtered, each row is transformed into a `TaxiTrip` entity. 
- **Validation Trigger:** During transformation, the `entity.validate()` method is invoked.
- **Error Handling:** Rows that fail universal validation are redirected to an "Audit Log" rather than crashing the pipeline.