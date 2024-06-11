FROM python:3.11.6-bullseye

ENV GECKODRIVER_VERSION=0.31.0
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/flaskapp/.local/bin

RUN useradd --create-home --home-dir /home/flaskapp maximosat

WORKDIR /home/flaskapp

USER maximosat
RUN mkdir app

COPY ./app ./app
COPY ./app.py .

ADD requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --user -r requirements.txt
RUN pip install gevent gunicorn==22.0.0


EXPOSE 5000

CMD ["gunicorn", "--workers", "1", "--log-level", "INFO", "--bind", "0.0.0.0:5000" ,"app:create_app()"]