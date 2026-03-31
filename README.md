# AI Spam Classifier

A full-stack application that classifies emails and messages as spam or legitimate using AI. Built with an Angular frontend and a Python FastAPI backend.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Angular 20, TypeScript 5.9, Tailwind CSS 4 |
| Backend | Python, FastAPI 0.135, Uvicorn |
| Validation | Pydantic v2, email-validator |
| Monitoring | Sentry SDK |

## Project Structure

```
AI Spam Classifier/
├── apps/
│   ├── backend/          # FastAPI REST API
│   │   ├── .env          # Environment variables (not committed)
│   │   └── requirements.txt
│   └── frontend/         # Angular SPA
│       ├── src/
│       │   ├── app/      # Components, routes, config
│       │   ├── main.ts
│       │   └── styles.css
│       ├── angular.json
│       └── package.json
├── .gitignore
├── README.md
└── TASKS.md
```

## Getting Started

### Prerequisites

- Node.js 20+
- Python 3.11+
- npm

### Backend

```bash
# Create and activate virtual environment
python -m venv apps/backend/.venv
source apps/backend/.venv/bin/activate    # macOS/Linux
apps\backend\.venv\Scripts\activate   # Windows

# Install dependencies
pip install -r apps/backend/requirements.txt

# Configure environment
cp apps/backend/.env.example apps/backend/.env
# Edit apps/backend/.env with your values

# Start the development server (from repository root)
fastapi dev apps/backend/main.py
```

The API will be available at `http://localhost:8000`.
Interactive docs: `http://localhost:8000/docs`

### Frontend

```bash
cd apps/frontend

# Install dependencies
npm install

# Start the development server
npm start
```

The app will be available at `http://localhost:4200`.

## Environment Variables

Create `apps/backend/.env` based on `.env.example`:

| Variable | Description |
|----------|-------------|
| `SENTRY_DSN` | Sentry DSN for error tracking |
| `ALLOWED_ORIGINS` | Comma-separated list of allowed CORS origins |
| `AI_API_KEY` | API key for the AI/ML classification service |

## Scripts

### Backend

| Command | Description |
|---------|-------------|
| `fastapi dev apps/backend/main.py` | Start dev server with hot reload |
| `fastapi run apps/backend/main.py` | Start production server |
| `pytest` | Run tests |

### Frontend

| Command | Description |
|---------|-------------|
| `npm start` | Start dev server on port 4200 |
| `npm run build` | Production build |
| `npm test` | Run Jasmine/Karma unit tests |
| `npm run watch` | Watch mode build |

## Architecture Notes

- **Frontend**: Uses Angular signals and zoneless change detection. Components are standalone by default.
- **Backend**: FastAPI with Pydantic v2 for request/response validation. WebSocket support included for real-time updates.
- **Communication**: REST API between frontend and backend; WebSocket channel for streaming classification results.
