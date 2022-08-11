FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY . /app

# No docker-compose approach
# ENV MONGO_USER='abc'
# ENV MONGO_PASS='abc'
# ENV MONGO_DB='abc'
# ENV MONGO_SERVER='abc'

EXPOSE 8005

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8005"]

#docker build . -t workshop-server   
#docker run -p 8005:8005 workshop-server