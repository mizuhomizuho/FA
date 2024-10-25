
async def app(scope, receive, send):

    assert scope['type'] == 'http'

    if scope['method'] == 'GET' and scope['path'] == '/script.js':
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'application/javascript'],
            ],
        })
        body: str = f'// Received {scope["method"]} request to {scope["path"]}\n'
        with open('src/script.js', 'br') as f:
            await send({
                'type': 'http.response.body',
                'body': body.encode('utf-8') + f.read(),
            })
        return

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/html'],
        ],
    })
    body = f'Received {scope["method"]} request to {scope["path"]}<script src="/script.js"></script>'
    await send({
        'type': 'http.response.body',
        # 'body': b'Hello, world!',
        'body': body.encode('utf-8'),
    })