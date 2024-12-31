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

# Ensure the correct permissions (optional for some platforms)
RUN chmod -R 755 /app

# Collect static files
RUN python manage.py collectstatic --noinput --clear

# Expose the application's port
EXPOSE 8080

# Add the ENTRYPOINT for running the application
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8080", "ProFileHub.wsgi:application"]
