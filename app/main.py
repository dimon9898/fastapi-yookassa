import json
from fastapi import FastAPI, HTTPException, Request, status



app = FastAPI()


@app.post('/webhook')
async def payment_webhook(request: Request):
    data = await request.json()
    result = json.dumps(data, indent=4, ensure_ascii=False)
    print(result)
    return {'ok': True}


