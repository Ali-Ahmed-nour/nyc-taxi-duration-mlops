# Testing Strategy: Property-Based Reliability

## 1. The Testing Hierarchy
- **Unit Tests:** Individual logic verification.
- **Property-Based Tests (PBT):** Stress-testing invariants via **Hypothesis**.
- **Integration Tests:** End-to-end flow from Polars to ML Adapters.

## 2. Mocking & Data Factories (Factory-Boy)
We utilize **Factory-Boy** as our "Synthetic Data Engine". 
- **Role:** It creates consistent, high-fidelity `TaxiTrip` objects for testing without manual dictionary creation.
- **Scalability:** As we add new models (Tip, Cancellation), we simply update the Factory to include new default attributes, ensuring all tests remain compatible.
- **Integration with Hypothesis:** We use `hypothesis.strategies.builds(TaxiTripFactory)` to combine the structure of a Factory with the randomness of PBT.

## 3. The 3-Zone Edge Case Coverage
Using **Hypothesis**, we mutate the Factory-generated data to explore:
1. **The Safe Zone:** Valid trips (Safe Defaults).
2. **The Edge Zone:** Extreme but legal values (Boundary testing).
3. **The Danger Zone:** Illegal values (Triggering `ERR_DOM_VAL`).

## 4. CI/CD & Static Guardrails
- **Linters:** **Ruff** for sub-second code cleaning.
- **Type Checking:** **Pyright** to ensure strict typing across the multi-model pipeline.
- **Coverage:** Mandatory 100% on `02_Domain_Core`.