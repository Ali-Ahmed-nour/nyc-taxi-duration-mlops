# Global Manifesto: The Sovereign Tech Stack

## 1. Governance
This manifesto defines the official tools and standards for the NYC Taxi Predictive Platform. Any deviation must be approved by the "Technical Committee."

## 2. Execution Environment
- **Runtime:** Python 3.12.3 (Strict).
- **Environment Manager:** **uv** (Mandatory). 
  - *Why:* Sub-second dependency resolution and PEP-517 compliance.
- **Project Structure:** `pyproject.toml` is the sole source of truth for dependencies.

## 3. Data & ML Core
- **Data Engine:** **Polars** (Lazy API). No Eager execution in production.
- **ML Engines:** Multi-engine support for **XGBoost**, **CatBoost**, and **Scikit-Learn**.
- **Optimization:** **Hyperopt** for automated tuning.
- **Tracking:** **MLflow** protocol for experiment lineage and model registry.

## 4. Quality & Language Standards
- **Coding Style:** Clean Code (Uncle Bob) principles.
- **Comments:** Strictly **English** (Mandate 2025-12-28).
- **Quality Guardrails:** - **Ruff:** Fast linting.
    - **Pyright:** Static type safety.
    - **Hypothesis:** Property-based testing.
    - **Factory-Boy:** High-fidelity data mocking.

## 5. Scalability Clause
The platform is designed to be **Task-Agnostic**. The addition of new prediction models (e.g., Tip, Fare, Cancellation) must not require changes to the `Domain Core` or the `Data Ingestion` logic, only the creation of new `Infrastructure Adapters`.