FROM egeselcuk/quiz_cli_bashfile:latest

# Install required packages
RUN pip install toml termcolor

# Create app directory
WORKDIR /app

# Copy all directories to /app
COPY ./ /app/

# Execute the delete_directories.sh script
RUN /app/delete_directories.sh

# Delete delete_directories.sh file
RUN rm /app/delete_directories.sh

# Set entry point to start the container in interactive mode with main.py
#CMD [ "python", "-i", "main.py" ]
