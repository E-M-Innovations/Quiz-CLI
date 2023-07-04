FROM python:3.11-slim-buster

# Install required packages
RUN pip install toml termcolor

# Create app directory
WORKDIR /app

# Copy Python files
COPY ./*.py ./

# Run a shell command to find directories containing TOML files and copy them to /app
RUN find . -type f -name '*.toml' -not -path './docs/*' -exec sh -c 'mkdir -p "/app/$(dirname "{}")" && cp "{}" "/app/$(dirname "{}")"' \;

# Set entry point to start the container in interactive mode with main.py
CMD [ "python", "-i", "main.py" ]
