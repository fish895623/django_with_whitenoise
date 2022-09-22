Start Up
```sh
gunicorn app.asgi:application -k uvicorn.workers.UvicornWorker
```
