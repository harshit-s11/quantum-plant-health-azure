# 🌿 Quantum Plant Health Classifier  
### Microsoft Azure Cloud Deployment Project

![CI Status](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci.yml/badge.svg)

---

## 📌 Project Overview

This project implements a **Quantum Machine Learning-based Plant Health Classification System** deployed using Microsoft Azure cloud services.

The system classifies tomato leaf images as:

- 🌱 Healthy  
- 🍂 Diseased  

The machine learning model is built using:

- Qiskit (Variational Quantum Classifier)
- Scikit-learn (PCA, accuracy metrics)
- Flask (REST API)
- Docker (Containerization)
- Microsoft Azure (Cloud Hosting Architecture)

---

## 🚀 Objective

To design and deploy a cloud-native AI solution using:

- Quantum Machine Learning
- Azure Cloud Services
- CI/CD Pipeline
- Containerized Deployment

This project demonstrates end-to-end AI deployment architecture suitable for enterprise environments.

---

## 🧠 Machine Learning Approach

### Models Implemented

| Model | Qubits | Image Size | Purpose |
|--------|--------|------------|----------|
| Fast VQC | 4 | 32x32 | Faster training |
| Improved VQC | 6 | 64x64 | Higher accuracy |
| Basic VQC | 2 | 16x16 | Lightweight baseline |

### Accuracy Calculation

Accuracy is calculated using:
Accuracy = (Correct Predictions) / (Total Predictions)
Using `sklearn.metrics.accuracy_score`.

---

## 🏗 Azure Architecture
User → Azure App Service → Flask API
↓
Azure Blob Storage
↓
Trained VQC Model


### Azure Services Used

- Azure App Service (Linux)
- Azure Blob Storage
- Azure Resource Group
- Azure CLI
- GitHub Actions CI/CD

---

## 📂 Project Structure
quantum-plant-health-azure/
│
├── app/
│ ├── app.py
│ ├── model_service.py
│
├── docker/
│ └── Dockerfile
│
├── infra/
│ ├── azure_setup.md
│ ├── blob_setup.py
│
├── .github/workflows/
│ └── ci.yml
│
├── requirements.txt
├── run.py
└── README.md


---

## 🐳 Docker Support

The application is containerized using Docker for consistent deployment.

To build locally:

```bash
docker build -t quantum-plant .
docker run -p 8000:8000 quantum-plant
