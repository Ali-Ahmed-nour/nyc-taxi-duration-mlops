# Hexagonal Layers: The Isolation Mandate

## 1. Architecture Philosophy
To build a scalable platform, we enforce a **Dependency Rule**: Dependencies must only point **INWARDS**. The Core should never know about the database, the ML framework, or the API.

## 2. The Three Sovereign Layers

### A. The Domain Core (The Sanctuary)
- **Role:** Contains the business logic, entities (`TaxiTrip`), and universal constants.
- **Rules:** - No external library imports (except standard Python).
    - Contains "Functional Core" logic (Pure functions, immutable data).
    - **Stability:** This is the most stable part of the system.

### B. The Application Layer (The Orchestrator)
- **Role:** Defines the **Ports** (Interfaces). 
- **Ports:** - `TripRepositoryPort`: Interface for loading data.
    - `InferencePort`: Interface for making predictions.
- **Responsibility:** Coordinates how data flows from the repository to the domain and then to the models.

### C. The Infrastructure Layer (The Laborers)
- **Role:** Implements the Adapters.
- **Components:**
    - **Data Adapters:** Polars-based parquet scanners.
    - **ML Adapters:** Specific implementations for XGBoost, CatBoost, etc.
    - **API Adapters:** Flask/FastAPI implementation for serving.
- **Rules:** This layer is the "Disposable" part. We can swap Flask for FastAPI without touching the Domain.

## 3. Communication Flow
1. **Request:** Comes through an Infrastructure Adapter (e.g., API).
2. **Orchestration:** Application layer calls the Data Adapter to get a `TaxiTrip`.
3. **Execution:** The Domain validates the trip.
4. **Inference:** The Application layer hands the trip to an ML Adapter.
5. **Response:** The result is stored in the `predictions_registry` and returned.