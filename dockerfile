FROM python:3.11.6-bullseye

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]