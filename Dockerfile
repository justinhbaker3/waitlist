FROM python:3.10

WORKDIR /waitlist

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /waitlist/babelfishbanking

COPY babelfishbanking /waitlist/babelfishbanking

EXPOSE 8000

RUN ["python", "manage.py", "migrate"]

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]