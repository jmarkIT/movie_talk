FROM python:3.12

WORKDIR /app

COPY pyproject.toml .

RUN pip install --no-cache-dir .

COPY . .

EXPOSE 8000

CMD ["gunicorn", "movie_talk.wsgi", "--bind", "0.0.0.0:8000"]
