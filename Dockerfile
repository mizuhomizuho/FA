FROM 3.12-slim

COPY . .

RUN pip install -r requirements.txt

CMD ['uvicorn', 'main:app', '--reload', '--port', '80', '--host', '0.0.0.0']