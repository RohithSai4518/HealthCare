# HealthSphere Production Container Image
FROM python:3.11-slim-bullseye

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000 \
    HOST=0.0.0.0

# Set working directory
WORKDIR /app

# Install security updates and dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency manifests
COPY requirements.txt requirements-lock.txt pyproject.toml setup.py /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . /app/

# Expose HTTP service port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/api/health || exit 1

# Run API server with synthetic seed
CMD ["python", "main.py", "--serve", "--host", "0.0.0.0", "--port", "8000"]
