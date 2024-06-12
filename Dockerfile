FROM python:3.12

WORKDIR ./


COPY test .

CMD ["python", "./calculator.py"]