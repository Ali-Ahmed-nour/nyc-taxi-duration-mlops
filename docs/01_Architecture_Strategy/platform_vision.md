# Platform Vision: The Multi-Model ML Engine

## 1. Executive Summary
This platform is designed to be a **Unified Inference Hub** for NYC Taxi operations. Unlike traditional ML scripts, this architecture treats models as "swappable plugins" that can be attached to a single, high-performance data stream.

## 2. Core Objective: From MVP to Scale
- **Phase 1 (MVP):** Deploy a `Trip Duration` prediction engine using the Sovereign Domain Entity.
- **Phase 2 (Growth):** Add `Tip Amount` and `Cancellation Probability` models without altering the core infrastructure.
- **Phase 3 (Enterprise):** Support real-time streaming inference using the same unified logic.

## 3. Design Principles
- **Entity Centrality:** The `TaxiTrip` entity is the single source of truth. All models must feed from and write back to this entity.
- **Agnostic Logic:** The system does not care which library (XGBoost, CatBoost, Scikit-Learn) makes the prediction, as long as it respects the `PredictionProtocol`.
- **Infrastructure-as-a-Detail:** Databases, API frameworks (Flask/FastAPI), and tracking tools (MLflow/W&B) are interchangeable adapters.

## 4. The "Model Registry" Concept
Every prediction task (e.g., Duration, Fare, Tip) is registered within the platform. The platform handles:
1. Data Fetching (via Polars).
2. Domain Validation.
3. Parallel Model Execution.
4. Unified Result Aggregation.