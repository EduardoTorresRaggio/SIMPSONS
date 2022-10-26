FROM python



RUN mkdir /app
WORKDIR /app
RUN mkdir Homer
RUN mkdir Lisa
RUN mkdir General

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade pip

CMD ["python","Maggie.py"]


