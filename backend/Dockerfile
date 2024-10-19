FROM python:3.9

# Set the current working directory to /app
WORKDIR /app

# Copy the files from the current directory(where this Dockerfile is located to the /app directory of the container)
COPY . .

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8000

CMD ["fastapi", "run", "--workers", "4", "main.py"]