import uvicorn

if __name__ == '__main__':

    uvicorn.run(
        'src.main:app',
        host='0.0.0.0',
        port=8009,
        # reload=True,
    )

# import pathlib
# import subprocess
# import sys
#
# if __name__ == '__main__':
#
#     proc_api = subprocess.Popen(f'python {pathlib.Path(__file__).parent.resolve()}/start_api.py',
#         shell=True, stdin=subprocess.PIPE, stdout=sys.stdout, stderr=sys.stdout)
#
#     proc_site = subprocess.Popen(f'python {pathlib.Path(__file__).parent.resolve()}/start_site.py',
#         shell=True, stdin=subprocess.PIPE, stdout=sys.stdout, stderr=sys.stdout)
#
#     while True:
#         pass

r'''
python -m venv .venv
cd C:\Users\xxxx0\PycharmProjects\FA && .venv\Scripts\activate && uvicorn main:app --reload --port 8009
Taskkill /IM uvicorn.exe /F
Taskkill /F /PID 11628
Get-Process -Id (Get-NetTCPConnection -LocalPort 30002).OwningProcess
netstat -ano|findstr "PID :8004"
taskkill /pid 3864 /f
tasklist /svc /FI "ImageName eq app*"
'''

r'''
docker system prune
docker build . --tag fa_app
docker-compose up
docker run -d -p 80:80 fa_app
docker run -p 80:80 -v C:\Users\xxxx0\PycharmProjects\FA:/FA:ro fa_app
docker logs fa_app
docker container exec -u 0 -it fa_python bash
'''

'''
alembic - A database migration tool for SQLAlchemy.
psycopg2 - Python-PostgreSQL Database Adapter (linux: psycopg2-binary)
'''

'''
alembic init migrations (cd src ; alembic init alembic)
alembic revision --autogenerate -m "meow"
alembic upgrade 482575c8ac4c
alembic upgrade head
'''

'''
asyncpg - An asyncio PostgreSQL driver
fastapi-users - Ready-to-use and customizable users management for FastAPI
'''

'''
redis-cli
keys *
set xxx 123
get xxx
del xxx
'''

'''
celery - Distributed Task Queue.
flower
celery -A src.tasks.tasks:celery worker --loglevel=INFO
celery -A src.tasks.tasks:celery worker --loglevel=INFO --pool=solo (для windows)
celery -A src.tasks.tasks:celery flower
'''

'''
pytest -v ./tests
pytest -v -s ./tests (для print)
'''