FROM python:3.6

COPY . /sidecar

WORKDIR /sidecar

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN ln -sf /dev/stdout /sidecar/hello_healthcheck.log

EXPOSE 80

CMD ["python3", "healthcheck.py"]




