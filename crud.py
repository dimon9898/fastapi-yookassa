import uuid
import httpx 


YOOKASSA_ID = '1170930'
YOOKASSA_SECRET_KEY = 'test_pWCcBYZluEj9oylfl8E76CKzGI_M3Qjh0EZbZfmfLHo'
YOOKASSA_URL = 'https://api.yookassa.ru/v3/payments'


async def generate_url(amount: float, user_id: int, user_name: str, course_id: int, return_url: str):
    idempotence = str(uuid.uuid4())
    
    headers = {
        'Idempotence-Key': idempotence
    }
    
    auth = (YOOKASSA_ID, YOOKASSA_SECRET_KEY)
    
    
    payload = {
        'amount': {
            'value': f'{amount:.2f}',
            'currency': 'RUB'
        },
        
        'confirmation': {
            'type': 'redirect',
            'return_url': return_url
        },
        
        'payment_method': {
            'type': 'sbp'
        },
        
        'capture': True,
        'description': f'Курс {course_id}',
        'metadata': {
            'user_id': user_id,
            'user_name': user_name,
            'course_id': course_id
        }
    }
    
    
    async with httpx.AsyncClient() as client:
        response = await client.post(YOOKASSA_URL, headers=headers, auth=auth, json=payload)
        
        data = response.json()
        
        return data