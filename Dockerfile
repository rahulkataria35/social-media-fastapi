FROM python:3.9


WORKDIR /app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir psycopg2-binary sqlalchemy alembic

COPY . .

COPY ./entrypoint.sh .

CMD ["./entrypoint.sh"]