FROM python:3.11-slim

WORKDIR /app

COPY appe.py .

CMD ["python", "appe.py"]
