FROM gcr.io/distroless/python3-debian10
ADD main.py /app/main.py
WORKDIR /app
CMD ["/app/main.py"]
