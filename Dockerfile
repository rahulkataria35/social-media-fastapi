FROM python:3

WORKDIR /app

# Copy requirements.txt and install dependencies
COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r ./requirements.txt

# Copy the entire project directory
COPY . .

# Set working directory within the container to the app directory
WORKDIR /app/app

# Expose the port for FastAPI application (adjust as needed)
EXPOSE 8000
EXPOSE 9092

# Run the command to start your application
CMD [ "python3", "main.py"]
