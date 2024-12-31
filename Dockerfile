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

# Copy requirements file and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput --clear

# Expose the application's port
EXPOSE 8080

# Set default Gunicorn parameters (Optional but good practice)
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:8080 --workers=3"

# Define the command to run the application
CMD ["gunicorn", "ProFileHub.wsgi:application"]
