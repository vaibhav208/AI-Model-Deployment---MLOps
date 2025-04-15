# Assignment 8: AI Model Deployment & MLOps

## 🎯 Objective
Deploy a sample AI model using **Docker** & **Kubernetes**, and expose it via an API endpoint.

---

## ✅ Deliverables

- Dockerfile & Kubernetes YAML files
- Steps to deploy the model
- Screenshot of the model running on Kubernetes

---

## 📁 Folder Structure

- `model/`: Python script to train and save the model
- `app/`: FastAPI app, requirements, Dockerfile
- `k8s/`: Kubernetes deployment & service files
- `screenshots/`: Add Kubernetes UI or Postman test screenshots here

---

## 🛠️ Setup Instructions

### 1. Train the Model

```bash
cd model
python train.py
```

### 2. Build Docker Image

```bash
docker build -t your-dockerhub-username/ai-model:latest -f app/Dockerfile .
docker push your-dockerhub-username/ai-model:latest
```

### 3. Deploy on Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 4. Test the API

```bash
curl -X POST http://<service-ip>:<port>/predict \
    -H "Content-Type: application/json" \
    -d '{"data": [5.1, 3.5, 1.4, 0.2]}'
```

Or open with Minikube:
```bash
minikube service ai-model-service --url
```

---

## 📸 Screenshots
Add dashboard or Postman screenshots inside `screenshots/`.