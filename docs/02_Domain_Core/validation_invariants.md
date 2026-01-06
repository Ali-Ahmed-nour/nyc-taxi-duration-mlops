# Validation Invariants: The Guardrails of Truth

## 1. Universal Invariants (Global Laws)
These rules are non-negotiable and apply to every `TaxiTrip` entity, regardless of the model being used:
- **Spatial Integrity:** `trip_distance` must be $> 0$. Physical movement is required for a "trip" to exist.
- **Temporal Logic:** `dropoff_time` must be chronologically after `pickup_time`.
- **Identity:** `vendor_id` and `LocationIDs` must be non-null and valid strings/integers.

## 2. Model-Specific Constraints (Task Laws)
Since this is a multi-model platform, each prediction task may have its own "Quality Filter":

### A. Trip Duration Engine (MVP)
- **Constraint:** $1.0 \le \text{duration} \le 60.0$ minutes.
- **Rationale:** Outliers outside this range are often GPS errors or long-stays that bias the duration model.

### B. Future Models (Examples)
- **Tip Predictor:** Requires `payment_type` to be 'Credit Card' (Cash tips are often unrecorded).
- **Cancellation Model:** Requires historical `passenger_id` consistency.

## 3. Enforcement Strategy
- **Layer:** All validation occurs inside the **Domain Core**.
- **Action:** If a Universal Invariant fails, the entity is **Rejected** (Critical Error).
- **Action:** If a Model-Specific constraint fails, the entity is marked as **Ineligible** for that specific model but remains valid for others.

## 4. Error Mapping
| Violation | Code | Severity |
| :--- | :--- | :--- |
| Negative/Zero Distance | `ERR_VAL_UNIV_001` | High |
| Logical Time Reversal | `ERR_VAL_UNIV_002` | High |
| Outlier Duration | `ERR_VAL_TASK_001` | Medium (Skip Task) |