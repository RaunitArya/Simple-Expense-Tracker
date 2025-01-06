FROM python:3.8-slim-buster

# COPY src /app/

COPY . /app/

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "application.py"]