FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV FLASK_APP=app.py

EXPOSE 4000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000" ]
