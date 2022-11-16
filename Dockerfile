FROM python:3.10-buster

WORKDIR /liatrio_app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt


CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

