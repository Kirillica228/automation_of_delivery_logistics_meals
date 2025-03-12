from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello")
def hello():
    return {
        "message":"hello"
    }

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8081, log_level='error')