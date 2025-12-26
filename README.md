# Trend Insight API Server

FastAPI 기반의 API 서버입니다.

## 설치 방법

1.  Python 가상환경을 생성합니다:
    ```bash
    python -m venv venv
    ```

2.  가상환경을 활성화합니다:
    *   Windows: `.\venv\Scripts\activate`
    *   Mac/Linux: `source venv/bin/activate`

3.  의존성 패키지를 설치합니다:
    ```bash
    pip install -r requirements.txt
    ```

## 실행 방법

서버를 개발 모드로 실행하려면 다음 명령어를 사용하세요:

```bash
uvicorn app.main:app --reload
```

서버가 실행되면 다음 주소로 접속할 수 있습니다:

*   API 문서 (Swagger UI): http://127.0.0.1:8000/docs
*   ReDoc 문서: http://127.0.0.1:8000/redoc
