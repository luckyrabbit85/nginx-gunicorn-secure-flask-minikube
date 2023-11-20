# Use Python 3.12.0 on Debian Bullseye
FROM python:3.12.0-bullseye

# Update and install system packages (Debian Bullseye)
RUN apt-get update && apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/*

# Set the username to 'blackrabbit'
ENV USER=blackrabbit

# Create a non-root user and group named 'blackrabbit'
RUN groupadd -r $USER && useradd -r -g $USER $USER

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/home/$USER/flask_app:${PATH}"

# Set the working directory and copy project files
WORKDIR /home/$USER/flask_app
COPY . .

# Change ownership of the copied files to the 'blackrabbit' user
RUN chown -R $USER:$USER /home/$USER/flask_app

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Switch to the 'blackrabbit' user
USER $USER

# Expose port
EXPOSE 8000

# Define the command to start the application
CMD ["gunicorn", "--log-level", "debug", "-w", "1", "-b", "0.0.0.0:8000", "wsgi:app"]

