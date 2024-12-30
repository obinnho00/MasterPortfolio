# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc libpq-dev libssl-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the application's port
EXPOSE 8000

# Define the command to run the application
CMD ["gunicorn", "ProFileHub.wsgi:application", "--bind", "0.0.0.0:8000"]
