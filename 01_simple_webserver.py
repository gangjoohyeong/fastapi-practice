from fastapi import FastAPI
import uvicorn

# FastAPI 객체 생성
app = FastAPI()

# "/"로 접근하면 return을 보여줌
@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
    

# uvicorn 없으면 CLI에 아래 명령어 입력
# uvicorn 01_simple_webserver:app --reload

# uvicorn 넣으면 CLI에서 파이썬만 실행하면 됨
# python 01_simple_webserver.py

# 이게 GET 방식