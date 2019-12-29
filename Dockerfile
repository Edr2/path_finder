FROM python:3.6.8

RUN pip install -r requirements.txt

ADD . /code

WORKDIR /code

EXPOSE 5000

CMD python app.py