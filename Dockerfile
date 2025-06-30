FROM python:3.11-slim

WORKDIR /app

COPY stupid_script.py .

CMD ["python", "stupid_script.py"]
