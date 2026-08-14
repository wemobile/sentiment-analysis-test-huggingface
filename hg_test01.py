import os
import requests
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# 1. HF 토큰
HF_TOKEN = os.environ.get("HF_TOKEN", "").strip()
if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN이 없습니다. .env 파일에 HF_TOKEN=hf_... 형식으로 입력하세요.")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json",
}

# 2. 모델 ID (네임스페이스 포함)
MODEL_ID = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

# 3. ✅ router 정식 엔드포인트
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"

def sentiment(text: str):
    r = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": text},
        timeout=30,
    )

    print("status:", r.status_code)
    print("content-type:", r.headers.get("content-type"))
    print("text(head):", r.text[:200])

    # JSON 안전 파싱
    if r.headers.get("content-type", "").startswith("application/json"):
        return r.json()

    return {
        "error": "Non-JSON response",
        "status": r.status_code,
        "text_head": r.text[:200],
    }

print(sentiment("I don't think that I do not love using Hugging Face!"))
