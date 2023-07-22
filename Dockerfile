FROM python:3.10.12-alpine3.18
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py /app/main.py
WORKDIR /app
CMD ["python" , "/app/main.py"]
