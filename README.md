# Mana Rythu AI

Minimal prototype of the farmer query support system.

The backend uses adapter stubs for LLM, speech-to-text, text-to-speech and
computer vision. Select the LLM provider via `LLM_PROVIDER` env var (defaults to
`LOCAL`).

## Development

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Tests
Backend:
```bash
PYTHONPATH=backend pytest
```
Frontend unit tests:
```bash
cd frontend
npm test
```
Playwright e2e:
```bash
cd frontend
npx playwright install chromium
npm run playwright
```

### Docker
```bash
docker-compose up --build
```

## Postman
See `docs/postman_collection.json`.
