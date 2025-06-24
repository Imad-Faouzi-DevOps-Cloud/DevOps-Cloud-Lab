# Use a minimal official Python image as the base
FROM python:3.10-slim

# Set environment variables to prevent Python from writing .pyc files and to buffer logs (good for containers)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Copy dependency list first (for better caching during rebuilds)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your Flask app will run on
EXPOSE 5000

# Define the default command to run the app
CMD ["python", "main.py"]

