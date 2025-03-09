
FROM python:3.9-slim

WORKDIR /app

COPY personal-api.py .

EXPOSE 5550

RUN pip install flask

CMD ["python", "personal-api.py"]
