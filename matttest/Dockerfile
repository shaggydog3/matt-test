FROM python:3.7-alpine

WORKDIR /matttest
COPY matttest/requirements.txt .
RUN pip install -r requirements.txt
COPY matttest .
COPY k8s ./k8s/

CMD ["python","-m","pytest"]

