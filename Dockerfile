# Stage 1: Base Image
# Use an official Python slim image for a smaller footprint.
FROM python:3.9-slim
# Set the working directory inside the container
WORKDIR /app
# Set environment variables to prevent Python from writing .pyc files
ENV PYTHONPATH="/app"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy the requirements file first to leverage Docker's build cache.
# This layer is only rebuilt if requirements.txt changes.
COPY requirements.txt .
# Install system dependencies (e.g., for browser drivers if not using Selenium Grid)
# and Python dependencies.
RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code into the container
COPY . .
# Make the entrypoint script executable
# We will create this script in the next steps to handle parameters
COPY entrypoint.sh /app/entrypoint.sh
# FORCE convert the file to Linux format (removes \r)
RUN sed -i 's/\r$//' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
# Set the entrypoint for the container. This script will be executed when the container starts.
ENTRYPOINT ["/app/entrypoint.sh"]
# Default command if no other command is provided to the entrypoint.
# We will pass the actual pytest command via docker-compose.
CMD ["pytest"]

