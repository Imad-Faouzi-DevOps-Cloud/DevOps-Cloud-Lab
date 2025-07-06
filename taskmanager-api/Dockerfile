# Using a slim official Python image (smaller attack surface, faster builds)
FROM python:3.11-slim

# Setting environment variables to avoid Python writing .pyc files and buffering logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Setting working directory inside the container
WORKDIR /app

# Installing system dependencies for Python packages that require compilation (like psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
 && rm -rf /var/lib/apt/lists/*

# Pre-copy only the requirements file to use Docker cache for dependency layer
COPY requirements.txt .

# Installing Python dependencies with no cache to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application code into the container
COPY . .

# Exposing the port used by the FastAPI application
EXPOSE 8000

# Using CMD to run the FastAPI app using uvicorn — production-friendly setup
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
