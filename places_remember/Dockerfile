FROM python:3.10.4

COPY . /code

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn


RUN chmod +x scripts/entrypoint.sh


CMD ["sh", "scripts/entrypoint.sh"]