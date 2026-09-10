![Build](https://github.com/kkkate123/python-backend/actions/workflows/docker-build.yaml/badge.svg)

A simple Python backend application built with Flask.

The application exposes REST endpoints and is containerized using Docker.
A GitHub Actions workflow automatically builds and pushes the Docker image to Docker Hub after every push to the `main` branch.

---

## Project Structure

```
python-backend/
├── .github/
│   └── workflows/
│       └── docker-build.yaml
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

---

## Technologies

- Python 3.12
- Flask
- Docker
- GitHub Actions
- Docker Hub

---

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Returns application status |
| `/health` | Health check endpoint |
| `/info` | Returns application information |

---

## Run Locally (optional for verifying)

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python3 app.py
```

Default URL:

```
http://localhost:8080
```

---

## Build Docker Image

```bash
docker build -t kkkate123/python-backend:1.0.0 .
```

---

## Run Docker Container

```bash
docker run -p 8080:8080 kkkate123/python-backend:1.0.0
```

---

## CI Pipeline

GitHub Actions automatically:

- checks out the repository;
- logs in to Docker Hub;
- builds the Docker image;
- pushes the image to Docker Hub.

The workflow is triggered on every push to the `main` branch.
