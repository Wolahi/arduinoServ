FROM python:3.12

RUN mkdir /arduinoApp

WORKDIR /arduinoApp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

ENTRYPOINT ["./docker/entrypoint.sh"]

CMD gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000