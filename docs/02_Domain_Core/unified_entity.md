# Unified Domain Entity: TaxiTrip

## 1. The Single Source of Truth
The `TaxiTrip` entity is a **Sovereign Object** that represents a single journey. To ensure scalability, it is designed to hold multiple model outputs simultaneously.

## 2. Technical Blueprint (Python 3.12.3)
To handle millions of trips in memory (via Polars/Uv), the entity uses:
- **`__slots__`**: For extreme memory efficiency.
- **`frozen=True`**: To ensure data integrity across the pipeline.

## 3. The Scalable Schema
| Attribute | Type | Description |
| :--- | :--- | :--- |
| `trip_id` | `str` | Unique Identifier. |
| `vendor_id` | `str` | Taxi provider ID. |
| `spatial_data` | `LocationVO` | Value Object for Pickup/Dropoff. |
| `temporal_data` | `TimeVO` | Value Object for timestamps. |
| `trip_distance` | `float` | Distance in miles. |
| **`predictions`** | **`Dict[str, float]`** | **The Registry:** A map of model names to values. |

## 4. The Registry Pattern (Scaling Strategy)
Unlike traditional models, we do not add a new field for every model. Instead:
- If we predict **Duration**, we add: `predictions["trip_duration"] = 15.5`
- If we predict **Tip**, we add: `predictions["expected_tip"] = 5.0`
- If we predict **Cancellation**, we add: `predictions["cancel_prob"] = 0.02`

## 5. Domain Logic: Validation
The entity is responsible for its own sanity. It contains a `validate()` method that:
1. Checks if spatial and temporal data are consistent.
2. Ensures mandatory fields for ML (like distance) are present.
3. Throws a `SovereignDomainError` if invariants are violated.