import json
from fastapi import FastAPI, HTTPException, Request, status
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)


logger = logging.getLogger('fastapi')




app = FastAPI()


@app.post('/webhook')
async def payment_webhook(request: Request):
    data = await request.json()
    result = json.dumps(data, indent=4, ensure_ascii=False)
    logger.info(f'INFO: {result}')
    return {'ok': True}


