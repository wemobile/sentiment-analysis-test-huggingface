# Sentiment Analysis Test by Using a hugging face model

자세한 설명은 쥬피터 노트북 파일(`hg_test01.ipynb`)을 참조하세요.

## 🔑 사전 준비 (Hugging Face 토큰)

### 1️⃣ Hugging Face 토큰 발급

1. [Hugging Face Settings](https://huggingface.co/settings/tokens)에 접속
2. **New token** 버튼 클릭
3. 토큰 이름 설정 (예: `sentiment-analysis`)
4. **Role** 선택: `read` 권한으로 충분
5. **Create token** 클릭
6. 생성된 토큰 복사 (형식: `hf_xxxxxxxxxxxxx`)

### 2️⃣ .env 파일 설정

프로젝트 루트 디렉토리에 `.env` 파일을 생성하고, 다음과 같이 입력하세요:

```env
# Hugging Face API Token
HF_TOKEN=hf_YOUR_TOKEN_HERE
```

**예시:**
```env
HF_TOKEN=hf_...
```

> ⚠️ **주의**: `.env` 파일에는 민감한 정보가 포함되어 있으므로, **절대 git에 commit하지 마세요**. 
> `.gitignore` 파일에 `.env`가 포함되어 있는지 확인하세요.

### 3️⃣ 패키지 설치

```bash
pip install -r requirements.txt
```

## 🚀 소스 코드 실행

### Python 스크립트 실행:

```bash
python hg_test01.py
```

### Jupyter 노트북 실행:

```bash
jupyter notebook hg_test01.ipynb
```

## 📝 코드 구조

- `hg_test01.py`: 간단한 sentiment analysis 스크립트
- `hg_test01.ipynb`: 상세 설명이 포함된 Jupyter 노트북
- `.env`: Hugging Face 토큰 저장 (로컬 전용)
- `requirements.txt`: 필요한 패키지 목록

