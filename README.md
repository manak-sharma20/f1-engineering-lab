# F1 Engineering Lab 🏎️

A production-grade web platform for visualizing, simulating, and predicting
Formula 1 car performance using 3D visualization and machine learning.

## What This Project Does

- **3D Car Viewer** — inspect and rotate every F1 car from any season
- **Component Swapping** — mix chassis, engines, and aero from different teams
- **Driver Swapping** — put any driver in any car
- **AI Predictions** — predict lap times for hybrid car combinations that never existed
- **Race Simulation** — simulate qualifying and race pace

## Tech Stack

| Layer      | Technology                                      |
|------------|-------------------------------------------------|
| Frontend   | Next.js, TypeScript, React Three Fiber, Zustand |
| Backend    | FastAPI, PostgreSQL, Redis                       |
| ML         | XGBoost, Scikit-Learn, SHAP, MLflow             |
| Infra      | Docker, GitHub Actions, Oracle Cloud            |

## Project Status

🚧 **In active development** — follow the journal below for daily progress.

## Development Journal

| Date       | What Was Built                              |
|------------|---------------------------------------------|
| 2025-06-17 | Project setup, FastAPI skeleton, 3 routers  |

## Getting Started

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --reload
```

API docs available at: `http://localhost:8000/docs`

## Folder Structure