# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy dependency file first, then install
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

