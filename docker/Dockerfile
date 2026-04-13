FROM python:3.11-slim

WORKDIR /app

COPY app/app.py /app/app.py

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
