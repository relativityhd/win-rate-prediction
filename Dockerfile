FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app
ADD ./app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD ./app /app

RUN pip install -r requirements.txt