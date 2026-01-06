# Prediction Protocol: Model-Agnostic Interface

## 1. The Wrapper Philosophy
To ensure the Domain Core is never coupled to a specific ML library, every model must be wrapped in a **Model Adapter**. This adapter acts as a translator between the `TaxiTrip` entity and the model's `predict()` method.

## 2. The Universal Interface (The Port)
Every Prediction Adapter must implement the following standard methods:
- `load_artifacts()`: Pulls the model binary and metadata from the registry.
- `preprocess(entity: TaxiTrip)`: Converts the entity's attributes into the specific feature vector required by the model.
- `predict_batch(entities: List[TaxiTrip])`: Executes inference and updates the `predictions` registry in each entity.

## 3. Handling Heterogeneous Models
The protocol supports multiple engine types simultaneously:
| Model Task | Engine | Transformation Logic |
| :--- | :--- | :--- |
| **Trip Duration** | XGBoost | Tabular features -> Float (Minutes) |
| **Tip Estimate** | CatBoost | Categorical features -> Float (USD) |
| **Fraud Check** | Scikit-Learn | Binary Classification -> Probability |

## 4. Multi-Task Execution Flow
1. **Dispatcher:** The application layer identifies which models are "Active".
2. **Parallel Inference:** The system can run multiple adapters in parallel (e.g., predicting Duration and Tip at the same time).
3. **Registry Update:** Results are injected back into the `TaxiTrip.predictions` dictionary using the task name as the key.

## 5. Versioning Requirements
Every prediction must be tagged with a **Model Signature** (e.g., `duration_v1.0.2`). This ensures that if a prediction is saved to the database, we know exactly which version of the logic produced it.