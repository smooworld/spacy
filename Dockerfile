FROM pypy:latest
WORKDIR /app
COPY . /app
CMD python semantic.py