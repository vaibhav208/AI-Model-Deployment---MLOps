FROM python:3.9-slim

WORKDIR /app
COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .
COPY model/model.pkl .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]