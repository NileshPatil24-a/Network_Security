# Network Security

An End-to-End Machine Learning Pipeline designed to detect and classify network security threats and anomalies.

## 🚀 Project Overview

This project provides a robust, scalable machine learning system for analyzing network traffic data. It features a fully automated ML pipeline covering data ingestion, validation, transformation, model training, and evaluation. The system is exposed via a FastAPI web interface, allowing users to trigger training pipelines and perform bulk predictions on network data. Workflow orchestration is handled by Apache Airflow.

## 🎯 Problem Statement

Modern enterprise networks generate massive volumes of traffic every second. Manually monitoring this traffic to detect complex, distributed, or zero-day cyber threats is practically impossible. Traditional rule-based security systems often generate a high rate of false positives and struggle to adapt to evolving attack vectors. There is a critical need for an automated, intelligent system that can continuously analyze network data, identify malicious patterns, and flag anomalous behavior effectively.

## 💡 Proposed Solution

This project solves the challenge of manual network monitoring by deploying a scalable Machine Learning pipeline. 
- **Automated Detection:** It uses historical network data to train models that can automatically classify network traffic as "Normal" or "Threat", reducing the burden on human analysts.
- **Scalability & Orchestration:** By orchestrating data workflows with Apache Airflow, the system efficiently handles large, continuous streams of data.
- **Accessibility:** A FastAPI-driven web interface allows security analysts to easily upload bulk network datasets and receive immediate, actionable predictions without needing deep technical expertise in machine learning.

## ✨ Features

- **End-to-End ML Pipeline**: Automated processes for data ingestion, validation, transformation, and model training.
- **FastAPI Web Interface**: A modern, responsive dashboard for interacting with the application.
- **Bulk Prediction**: Upload CSV datasets to get immediate batch predictions on network traffic (threat vs. normal).
- **Workflow Orchestration**: Integrated with Apache Airflow for scheduling and monitoring background tasks.
- **Cloud Integration**: Stores data and artifacts securely using AWS S3 and MongoDB.
- **Containerized Deployment**: Fully dockerized environment for seamless deployment and reproducibility.

## 🛠️ Technology Stack

- **Language**: Python 3.10
- **Web Framework**: FastAPI
- **Machine Learning**: Scikit-learn, Pandas, Numpy
- **Orchestration**: Apache Airflow
- **Database**: MongoDB
- **Cloud Storage**: AWS S3
- **Containerization**: Docker & Docker Compose
- **Frontend**: HTML/CSS/JS (Jinja2 Templates)

## 📋 Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.10 or higher
- Docker and Docker Compose (for containerized execution)
- A MongoDB cluster (Atlas or local)
- AWS Account with S3 access

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Network_Security
```

### 2. Environment Variables

Create a `.env` file in the root directory and configure the necessary credentials:

```env
MONGO_DB_URL="your_mongodb_connection_string"
AWS_ACCESS_KEY_ID="your_aws_access_key"
AWS_SECRET_ACCESS_KEY="your_aws_secret_key"
AWS_DEFAULT_REGION="us-east-1"
BUCKET_NAME="mynetworksecurity-1"
```

### 3. Local Setup (Without Docker)

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

Run the FastAPI application:

```bash
python main.py
```

### 4. Docker Setup

To run the entire application stack (FastAPI + Airflow) using Docker:

```bash
# Set IMAGE_NAME variable and other required environment variables, then run:
docker-compose up --build
```

*Note: The Docker container will automatically start the Airflow scheduler, Airflow webserver (port 8081), and the FastAPI application (port 8080).*

## 💻 Usage

Once the application is running, you can access the following interfaces:

- **Web Dashboard**: `http://localhost:8080`
  - Navigate to the dashboard to upload network traffic CSV files for prediction.
- **Airflow Webserver**: `http://localhost:8081` (Credentials: `admin` / `admin`)
  - Monitor and manage scheduled machine learning pipelines.
- **FastAPI Docs (Swagger)**: `http://localhost:8080/docs`
  - Explore and test API endpoints directly.

### API Endpoints

- `GET /`: Loads the main web dashboard.
- `GET /train`: Triggers the machine learning training pipeline.
- `POST /predict`: Accepts a CSV file upload and returns bulk predictions for network threats.

## 📁 Project Structure

```text
Network_Security/
├── .github/                  # GitHub Actions CI/CD workflows
├── airflow/                  # Airflow DAGs and configuration
├── networksecurity/          # Core ML Pipeline Modules (Ingestion, Validation, etc.)
├── static/                   # Frontend static assets (CSS, JS)
├── templates/                # Jinja2 HTML templates
├── main.py                   # FastAPI application entry point
├── Dockerfile                # Docker image configuration
├── docker-compose.yaml       # Docker Compose setup
├── requirements.txt          # Python dependencies
├── setup.py                  # Package configuration
└── start.sh                  # Startup script for Docker container
```
