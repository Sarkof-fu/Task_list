from aiohttp import web


async def handle(request):
    id = request.match_info.get('id', "Anonymous")
    text = "Hello, " + id
    return web.Response(text=text)


async def sum_handler(request):
    data = await request.json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    s = num1 + num2
    return web.Response(text=str(s))


async def fibonachi(request):
    data = await request.json()
    length = data.get("length")


def main():
    app = web.Application()
    app.add_routes([web.get('/get-user/{id}', handle),
                    web.post('/sum', sum_handler),
                    web.post('/fibonachi', fibonachi)])
    web.run_app(app)


if __name__ == '__main__':
    main()