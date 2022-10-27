FROM python:3.10-slim

WORKDIR /users-api

COPY ./requirements.txt /users-api/equirements.txt
COPY ./app/users.py /users-api

RUN pip install --no-cache-dir --upgrade -r /users-api/equirements.txt

CMD ["uvicorn", "users:app", "--host", "0.0.0.0", "--port", "80"]
