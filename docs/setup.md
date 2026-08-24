# Setup Guide

## Prerequisites

- Python 3.13 or later
- pip or poetry
- FFmpeg (optional for Phase 1, required later)
- Git

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/sapekshkumarb/ai-shorts-factory.git
cd ai-shorts-factory
```

### 2. Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
# Edit .env with your settings
```

### 5. Run Application

```bash
python -m uvicorn app.main:app --reload
```

Application will start at `http://127.0.0.1:8000`

## Verification

### Health Check

```bash
curl http://127.0.0.1:8000/health
```

Expected response:
```json
{
  "status": "OK",
  "version": "0.1.0",
  "environment": "development",
  "debug": true
}
```

### Provider Health

```bash
curl http://127.0.0.1:8000/health/providers
```

## Running Tests

```bash
pytest
```

## Troubleshooting

### Python Version

Ensure Python 3.13+:
```bash
python --version
```

### Virtual Environment

Make sure venv is activated (you should see `(venv)` in your prompt).

### Module Not Found

Reinstall requirements:
```bash
pip install --force-reinstall -r requirements.txt
```

### Port Already in Use

Change port in `.env` or run:
```bash
python -m uvicorn app.main:app --port 8001 --reload
```
