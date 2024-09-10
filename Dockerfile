# Use Python 3.10 slim base image
FROM python:3.10-slim

# Set environment variables to avoid prompts during apt operations
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary system dependencies in a single layer and clean up afterward
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libmariadb-dev-compat \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy only the requirements file first to leverage Docker cache for dependencies
COPY requirements.txt /app/

# Upgrade pip and install dependencies from requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port the app will run on
EXPOSE 8000

# Define the default command to run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
