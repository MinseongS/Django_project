FROM python:3.10.6
WORKDIR .

RUN pip install -r requirements.txt

## Run the application on the port 50000
EXPOSE 50000

