# Use a lightweight official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy app folder content to /app/app inside the container
COPY app/ ./app

# Copy Python dependencies file
COPY app/requirements.txt .

# Install Python packages from requirements.txt
RUN pip install -r requirements.txt

# Define the command to run the Flask app
CMD ["python", "app/app.py"]
