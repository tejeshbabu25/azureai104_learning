FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "1_chat_models_input_from_docker_and_VMs:app", "--host", "0.0.0.0", "--port", "8000"]