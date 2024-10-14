# Use the official Python image as a base image
FROM python:3.11

COPY ./requirements.txt ./

# Install production dependencies.
RUN pip install -r requirements.txt

# Set the working directory within the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

CMD find ./src -name "*.py" -exec python {} \;