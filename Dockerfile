from python:3.6
RUN mkdir -p /app/architect_pg
ADD architect_pg /app/architect_pg
ADD requirements.txt /app/architect_pg
WORKDIR /app/architect_pg
RUN pip3 install -r requirements.txt
