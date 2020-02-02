# Base image
FROM python:3.7-slim

# Copy our app to containers /app path
# and use /app as a working directory
COPY . /app
WORKDIR /app

# Install requirements
RUN python3 -m pip install -r requirements.txt

# Run our app
CMD ["python3", "main.py"]