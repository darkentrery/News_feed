FROM python:3.9.6-alpine

WORKDIR /news_site

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install gunicorn
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /news_site/entrypoint.sh
RUN chmod +x /news_site/entrypoint.sh

COPY . .

ENTRYPOINT ["/news_site/entrypoint.sh"]
