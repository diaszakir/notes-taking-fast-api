from fastapi import FastAPI
from starlette import status

app = FastAPI()

@app.get('/test', response_class=status.HTTP_200_OK)
async def test_api():
    return {"message": "success"}