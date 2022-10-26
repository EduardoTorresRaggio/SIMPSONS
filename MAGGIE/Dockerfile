FROM python:latest

RUN mkdir /app
WORKDIR /app
RUN mkdir Homer
RUN mkdir Lisa
RUN mkdir General

COPY . /app

RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade pip

CMD ["python","Maggie.py"]


