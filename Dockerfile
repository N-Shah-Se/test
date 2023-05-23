FROM "python:3.7"

RUN mkdir /qr_faas_management

WORKDIR /qr_faas_management

COPY ./qr_faas_management /qr_faas_management

COPY requirements.txt /qr_faas_management/

RUN pip install -r requirements.txt

ADD . /qr_faas_management/



