# import uvicorn
#
# if __name__ == '__main__':
#
#     uvicorn.run(
#         'main:app',
#         host='0.0.0.0',
#         port=80,
#         reload=True,
#         reload_dirs=['/FA'],
#         access_log=False,
#     )

# cd C:\Users\xxxx0\PycharmProjects\FA && .venv\Scripts\activate && uvicorn main:app --reload --port 8009
# Taskkill /IM uvicorn.exe /F
# Taskkill /F /PID 11628
# Get-Process -Id (Get-NetTCPConnection -LocalPort 8004).OwningProcess
# netstat -ano|findstr "PID :8004"
# taskkill /pid 3864 /f
# tasklist /svc /FI "ImageName eq app*"

# docker build . --tag fa_app && docker run -p 80:80 fa_app

# docker run -p 80:80 -v C:\Users\xxxx0\PycharmProjects\FA:/FA:ro fa_app

# python -m venv .venv

# docker-compose up
