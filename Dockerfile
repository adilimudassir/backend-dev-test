FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY ./requirements.txt /code/

RUN pip install -U pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . /code

COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh" ]