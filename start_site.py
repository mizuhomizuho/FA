import uvicorn

if __name__ == '__main__':

    uvicorn.run(
        'src.main_site:app',
        host='0.0.0.0',
        port=8010,
        # reload=True,
    )