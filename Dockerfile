FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
USER root
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app/server.py"]
