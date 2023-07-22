FROM gcr.io/distroless/python3-debian10
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py /app/main.py
WORKDIR /app
CMD ["/app/main.py"]
