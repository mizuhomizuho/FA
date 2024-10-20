import uvicorn

if __name__ == '__main__':

    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8009,
        # reload=True,
    )

# python -m venv .venv
# cd C:\Users\xxxx0\PycharmProjects\FA && venv\Scripts\activate && uvicorn main:app --reload --port 8009
# Taskkill /IM uvicorn.exe /F
# Taskkill /F /PID 11628
# Get-Process -Id (Get-NetTCPConnection -LocalPort 30002).OwningProcess
# netstat -ano|findstr "PID :8004"
# taskkill /pid 3864 /f
# tasklist /svc /FI "ImageName eq app*"

# docker system prune
# docker build . --tag fa_app
# docker-compose up
# docker run -p 80:80 fa_app
# docker run -p 80:80 -v C:\Users\xxxx0\PycharmProjects\FA:/FA:ro fa_app
# docker container exec -u 0 -it fa-fa_app-1 bash

# python -m pip freeze > requirements_linux.txt
# python -m pip install -r requirements_linux.txt
# python -m pip freeze > requirements_win.txt
# python -m pip install -r requirements_win.txt

# alembic - A database migration tool for SQLAlchemy.
# psycopg2 - Python-PostgreSQL Database Adapter (linux: psycopg2-binary)

# alembic init migrations
# alembic revision --autogenerate -m "DB create"