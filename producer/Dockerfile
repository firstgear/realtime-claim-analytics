# Use the official Python 3.9 slim image
FROM python:3.9-slim

# Copy the current directory contents into the container at /app
COPY producer.py /app/

# Install the dependencies
RUN pip install kafka-python

# Run the application
CMD ["python", "/app/producer.py"]

