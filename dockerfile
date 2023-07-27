FROM python:3.11-buster

RUN pip install poetry

COPY . .

RUN poetry install

EXPOSE 8080

ENTRYPOINT ["poetry", "run", "python", "-m", "app"]
