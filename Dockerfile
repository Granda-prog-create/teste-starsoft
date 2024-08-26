FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 
COPY .env /app/.env


CMD ["python", "main.py"]
