# 🚕 STIE: Sovereign Taxi Inference Engine

### *The Sovereign Hexagonal Blueprint for Industrial ML*

> **"Architecture is the art of planning for the unknown. We don't just build code; we build sovereign digital assets."**

______________________________________________________________________

### 👤 Principal Architect & Strategic Inquiry

**Ali Ahmed Nour** *Principal Architect for Sovereign Hexagonal & DDD Systems*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/ali-ahmed-nour/)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-Connect-green?style=for-the-badge&logo=whatsapp)](https://wa.me/201007871314)
[![Phone](https://img.shields.io/badge/Direct_Line-01288061914-orange?style=for-the-badge&logo=phone)](tel:+201288061914)
[![Phone](https://img.shields.io/badge/Direct_Line_2-01007871314-red?style=for-the-badge&logo=phone)](tel:+201007871314)

______________________________________________________________________

### 🎯 The Sovereign Thesis

STIE is a Future-Proof engineered **Unified Inference Hub** designed for NYC Taxi operations. This platform represents an evolution from being "Agnostic" to being **Sovereign**.

In this architecture, the **Business Logic is the Sovereign Power**. We treat the core of the project as a **Sovereign Sanctuary** (Domain Core) with zero external dependencies. All external tools—Google Cloud, BigQuery, and MLflow—are merely **"interchangeable gears" (تروس)** that can be swapped without touching the system's heart.

## 💎 Strategic Core Values

- **Zero Vendor Lock-in:** The platform is **Cloud-Agnostic**, ensuring we own the Intellectual Property completely and can migrate to any environment without friction.
- **Multi-Model Scalability:** Designed to evolve from a single prediction engine to a **Unified Hub** (Duration, Tip, Cancellation) without altering the core infrastructure.
- **Industrial-Grade Reliability:** Protected by a "Sovereign Constitution," the system self-audits and rejects corrupted data instantly via **Universal Invariants**.
- **Economic Optimization:** Powered by the **Polars Lazy Engine** to reduce computational footprint, leading to lower infrastructure costs and higher processing speeds.
- **Institutional Transparency:** Full adherence to the **10-File Documentation Standard** ensures a permanent, audit-ready asset for any global team.

## ⚙️ Engineering & Operational DNA

#### 🛡️ Sovereign Hexagonal Implementation

- **Domain Core (The Sanctuary):** Zero external library imports; contains pure business logic and immutable entities.
- **Application Layer (The Orchestrator):** Defines **Strict Ports** (Interfaces) for data ingestion and inference.
- **Infrastructure Layer (The Laborers):** Implements swappable adapters for Polars, ML engines, and Cloud APIs.

#### ⚡ Performance & Data Integrity

- **Memory Efficiency:** All entities utilize `__slots__` and `frozen=True` (Python 3.12+) for extreme RAM optimization.
- **The Lazy Protocol:** Integration of **Polars Lazy API** with Projection and Predicate Pushdown to optimize query plans.
- **Registry Pattern:** Flexible storage for multiple model outputs using a `Dict[str, float]` within the core entity.

#### 🧪 Quality & MLOps Governance

- **Enterprise-Grade Code Quality:** Managed via **SonarQube** for continuous monitoring of Technical Debt and Security Hotspots.
- **Sovereign Error Taxonomy:** Every failure returns a deterministic code (e.g., `ERR_DOM_VAL_001`) for industrial-grade monitoring.
- **Shield Protocol:** Mandatory **Pre-commit Hooks** enforcing strict linting and safety gates before any persistence.
- **Security & Compliance:** **Mend (WhiteSource)** integration for continuous open-source vulnerability scanning.
- **Static Guardrails:** Strict **Pyright** static analysis to ensure 100% type-safety across the Sanctuary.
- **Test & Logic Integrity:** Enforced via **pytest** and **pytest-cov**, generating automated `.coverage` reports to verify every execution path.
- **Quality Suite:** Advanced stress testing powered by **Hypothesis** (PBT) and **Factory-Boy**.
- **Deterministic Environments:** Powered by **uv project** for reproducible and sovereign dependency management.
- **Model Provenance:** **MLflow** integration for full experiment lineage and automated registry promotion.

## 📂 Documentation & Execution

For deep architectural insights and technical governance, please refer to our **Sovereign Documentation Hub**:

- **[01_Architecture_Strategy](docs/01_Architecture_Strategy/hexagonal_layers.md):** Isolation mandates and dependency rules.
- **[02_Domain_Core](docs/02_Domain_Core/unified_entity.md):** Entity blueprints and validation invariants.
- **[03_Infrastructure_Adapters](docs/03_Infrastructure_Adapters/data_ingestion.md):** Data engines and prediction protocols.
- **[04_Quality_Assurance](docs/04_Quality_Assurance/error_codes.md):** Error taxonomy and testing strategy.

______________________________________________________________________

### 🚀 Quick Start

1. **Environment Setup:**

   ```bash
   uv sync # Mandatory environment manager
   source .venv/bin/activate

   ```

1. **Execute Quality Suite:**
   pytest # Runs Hypothesis (PBT) and Factory-Boy stress tests

## 🚧 Execution Roadmap (Folder-Mapped)

| Phase | Milestone | Strategic Objective | Target Context | Status |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Foundational DNA** | Environment Hardening, `uv` Project Setup & Security Guardrails. | `pyproject.toml`, `.pre-commit-config.yaml` | [✅] Done |
| **2** | **Structural Blueprint** | Defining Hexagonal Ports (Interfaces) for Ingestion & Inference. | `core/application/ports/` | [✅] Done |
| **3** | **Sovereign Brain** | **Crafting Domain Entities, Value Objects & Sovereign Exceptions.** | `core/domain/` | [🚀] **Ongoing** |
| **4** | **Orchestration Layer** | Implementing Core Use-Cases (Ingestion & Prediction Workflows). | `core/application/use_cases/` | [ ] Pending |
| **5** | **Infrastructure Adapters** | Developing Laborers for Polars, XGBoost, and MLflow Tracking. | `infrastructure/adapters/` | [ ] Pending |
| **6** | **Industrial Operations** | Integration, Central Config, and Enterprise-Grade QA (SonarQube). | `main.py`, `infrastructure/config/` | [ ] Pending |
