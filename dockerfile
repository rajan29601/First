# Dockerfile
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install flask

# Expose port 5000 so it can be accessed outside
EXPOSE 5000

# Command to run your app
CMD ["python", "app.py"]

