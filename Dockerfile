FROM python:3.9.18-slim
# FROM python:3.8.12-slim

# RUN apt-get update \
#     && apt-get install -y build-essential \
#     && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir pipenv
# RUN pip install --upgrade pipenv

WORKDIR /app

COPY ["Pipfile","Pipfile.lock","./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "model_eta=0.07.bin", "./"]

EXPOSE 9695

ENTRYPOINT [ "gunicorn","--bind=0.0.0.0:9695","predict:app"]