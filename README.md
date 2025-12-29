# 🚕 NYC Taxi Duration Prediction: End-to-End MLOps Pipeline

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![MLOps](https://img.shields.io/badge/MLOps-Engineering-orange.svg)](https://en.wikipedia.org/wiki/MLOps)
[![Environment Management](https://img.shields.io/badge/Managed%20by-uv-purple.svg)](https://github.com/astral-sh/uv)

A production-ready MLOps project designed to predict taxi trip durations in NYC. This project transitions from a research notebook to a robust, maintainable pipeline, emphasizing engineering excellence and reproducible workflows.

## 🎯 Business Problem
Predicting trip duration is critical for urban mobility services. Accurate estimates improve user experience, optimize driver dispatching, and enhance fare estimation. This project builds a baseline model to tackle this challenge using NYC Taxi & Limousine Commission (TLC) data.

## 🏗️ Architecture & Engineering Principles

This project is built with a **"Production-First"** mindset:
* **Single Source of Truth (SSoT):** A centralized configuration layer manages all paths, features, and model parameters, ensuring consistency across Training, Validation, and Inference.
* **Memory Optimization:** Implementation of vectorized downcasting to handle millions of rows with a minimum memory footprint (e.g., using `float32`).
* **Type Safety:** Fully typed using Python's `TypedDict` and verified with **Pylance** to catch bugs before runtime.

## 🛠️ Tech Stack
* **Environment:** [uv](https://github.com/astral-sh/uv) (Extremely fast Python package installer and resolver).
* **Data Science:** Pandas, NumPy, Scikit-learn.
* **Experiment Tracking:** MLflow (In progress).
* **Orchestration:** Prefect (In progress).
* **Formatting:** Ruff for linting and code quality.

## 🚀 Getting Started

### Prerequisites
Ensure you have `uv` installed. If not, install it via:
```bash
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh