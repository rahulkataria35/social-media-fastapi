FROM python:3

WORKDIR /app

# Copy requirements.txt and install dependencies
COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r ./requirements.txt
COPY ./alembic ./alembic
COPY ./alembic.ini ./alembic.ini
RUN alembic upgrade head


# Copy the entire project directory
COPY . .

# Set working directory within the container to the app directory
WORKDIR /app/app

# Run the command to start your application
CMD [ "python3", "main.py"]
