FROM python:3

RUN useradd -ms /bin/bash endpoint
ADD . /home/endpoint
WORKDIR /home/endpoint

RUN pip install -r requirements.txt
EXPOSE 8000

USER endpoint
CMD python read_endpoint_app.py 


