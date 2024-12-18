# Use official Python image from the Docker hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app to the working directory
COPY . .

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Start the FastAPI app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
