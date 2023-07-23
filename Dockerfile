FROM python:3.10.12-alpine3.18

COPY setup.py setup.py

COPY validator/ /validator/

RUN pip install .

WORKDIR /validator

CMD ["python" , "/validator/run.py"]
