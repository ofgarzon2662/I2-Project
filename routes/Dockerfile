FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install --upgrade pip \
    && pip install pipenv \
    && pipenv install

ENV FLASK_APP=./src/main.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=3002

EXPOSE 3002

CMD pipenv run flask run