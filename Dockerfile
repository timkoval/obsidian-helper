FROM python:3.11
WORKDIR /code
COPY pyproject.toml /code/pyproject.toml 
COPY ./app /code/app
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]