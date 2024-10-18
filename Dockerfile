FROM python:3.12-slim

RUN mkdir /FA

WORKDIR /FA

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Make port 8001 available to the world outside this container
EXPOSE 8001:8001

# Define environment variable
ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "main:app", "--port", "8001", "--host", "0.0.0.0", "--reload"]