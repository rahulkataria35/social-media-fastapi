FROM python:3.9.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir psycopg2-binary sqlalchemy alembic

COPY . ./usr/src/app

# CMD [ "python3", "-u", "./app/main.py" ]

COPY entrypoint.sh .

CMD ["./entrypoint.sh"]