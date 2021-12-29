import json
import urllib
import time
import asyncio
import aiohttp
import functools
import ssl
import json

async def fetchCreds(client, uri):
    async with client.post(uri) as resp:
        # assert resp.status == 200
        return await resp.text()

async def fetchGet(client, uri):
    async with client.get(uri) as resp:
        return await resp.text()

async def carousel(uri):
    ssl_ctx = ssl.create_default_context(cafile='ca-chain.pem')
    ssl_ctx.load_cert_chain('client-cert.pem', 'client-key.pem')

    conn = aiohttp.TCPConnector(ssl=ssl_ctx)
    url = uri + '/api/get/carousel'

    async with aiohttp.ClientSession(connector=conn) as client:
        text = await fetchCreds(client, url)
        return json.loads(text)

async def success_carousel(uri):
    ssl_ctx = ssl.create_default_context(cafile='ca-chain.pem')
    ssl_ctx.load_cert_chain('client-cert.pem', 'client-key.pem')

    conn = aiohttp.TCPConnector(ssl=ssl_ctx)
    url = uri + '/api/get/success'

    async with aiohttp.ClientSession(connector=conn) as client:
        return await fetchGet(client, url)

async def fetch_all(loop, numRequests, delay, url, body, headers):

    results = await asyncio.gather(*[fetch_one(loop, url, i, delay, body, headers) for i in range(1, numRequests + 1)], return_exceptions=True)

    return results

async def fetch_one(loop, url, iter, delay, body, headers):

    delay = iter * delay / 1000
    # print(" i'm waiting " + str(delay * 1000) + " ms")
    await asyncio.sleep(delay)

    async with aiohttp.ClientSession(loop=loop, headers=headers) as session:
            async with session.post(url, data = json.dumps(body)) as resp:
                # print("An api call to ", url, " is made at ", time.time())
                # print(await resp.text())
                text = await resp.text()
                # print('Request with num ' + str(iter) + ' completed')
                # print(1)
                return text

def lambda_handler(event, context):
    # delay = 200 # ms
    # numRequests = 20 # req num
    # saleTime = 1639479599
    # json_dumps(event)
    carousel_uri = event['queryStringParameters']['carousel_uri']

    loop = asyncio.get_event_loop()
    fetched = loop.run_until_complete(carousel(carousel_uri))

    numRequests = fetched['settings']['numRequests']
    delay = fetched['settings']['delay']
    saleTime = fetched['settings']['saleTime']

    url = fetched['settings']['url']
    body = fetched['settings']['body']

    headers = fetched['headers']
    print(headers)
    print(url)
    print(body)
    # return
    # loop = asyncio.get_event_loop()

    while True:
        ts = time.time() * 1000
        print(ts)
        print(saleTime)
        if saleTime<ts:
            break

    results = loop.run_until_complete(fetch_all(loop, numRequests, delay, url, body, headers))

    for result in results:
        try:
            success = json.loads(result)['success']
            if success:
                print("Success!")
                fetched = loop.run_until_complete(success_carousel(carousel_uri))
        except Exception:
            print('Cant parse' + result)

    return {
        "res": results
    }

event = []
event = {
  "queryStringParameters": {
    "carousel_uri": "https://localhost:4433"
  }
}
print(lambda_handler(event,1))
