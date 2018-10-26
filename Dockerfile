FROM python:3

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python app.py --port 8000


