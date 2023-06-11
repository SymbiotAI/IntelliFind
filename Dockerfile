# Stage 1: Build
FROM python:3.9-slim-buster as builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc

# Install python dependencies
COPY requirements.txt .
RUN pip install --user --no-warn-script-location -r requirements.txt

# Stage 2: Runtime
FROM python:3.9-slim-buster as runtime

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy over the installed python dependencies from the builder stage
COPY --from=builder /root/.local /root/.local

# Make sure scripts in .local are usable:
ENV PATH=/root/.local:$PATH

# Copy your application code to the container (make sure you create a .dockerignore)
COPY . .

# Run your script
CMD ["python", "/app/main.py"]
