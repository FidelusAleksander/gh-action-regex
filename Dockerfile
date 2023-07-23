FROM python:3.10.12-alpine3.18
COPY setup.py setup.py
RUN pip install .
COPY validator/ /validator/
WORKDIR /validator
CMD ["python" , "/validator/main.py"]
