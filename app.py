from flask import Flask, Response, request
from flask_cors import CORS
import json
import logging
import time
import asyncio


from application_services.Sync.sync_service import SyncService
from application_services.Async.async_service import AsyncService

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'


# post a composed info to 3 microservices synchronously
@app.route('/composer/sync', methods=['POST'])
def post_all_sync():
    if request.method == 'POST':
        create_data = request.form
        if create_data:
            pass
        else:
            create_data = request.json[0]
        res = SyncService.postall(create_data)
        rsp = Response(json.dumps(res, default=str), status=201, content_type="application/json")
        return rsp

# post a composed info to 3 microservices asynchronously
@app.route('/composer/async', methods=['POST'])
def post_all_async():
    if request.method == 'POST':
        create_data = request.form
        if create_data:
            pass
        else:
            create_data = request.json[0]
        s = time.perf_counter()
        asyncio.run(AsyncService.postall(dict(create_data)))
        elapsed = time.perf_counter() - s
        print(f"Executed in {elapsed:0.2f} seconds.")
        rsp = Response(json.dumps("success", default=str), status=201, content_type="application/json")
        return rsp

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
