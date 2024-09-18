# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's source code to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
