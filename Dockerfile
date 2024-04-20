FROM python:3.9

WORKDIR /app

COPY backend/ .

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8080

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0", "main:app", ":8080"]
