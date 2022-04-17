FROM python:3.10-alpine

COPY . /app
WORKDIR /app
RUN python3 -m pip install pipenv \
    && pipenv install --system
EXPOSE 5000
CMD ["flask", "run"]