# Use official Python image
FROM python:3.10

# Set work directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Run app
CMD ["python", "app.py"]




