# Use official Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy only dependencies file first (for caching)
COPY app/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY app/ .

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "main.py"]
