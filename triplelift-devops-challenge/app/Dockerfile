FROM python:3.6

# app listening on port 8080
EXPOSE 8080

COPY . /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV FLASK_APP=hello.py

ENV FLASK_RUN_PORT=8080

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]


