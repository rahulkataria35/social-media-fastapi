FROM python:3.9.7
WORKDIR /app
COPY ./requirements.txt ./requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
RUN alembic upgrade head

CMD [ "python3", "main.py" ]