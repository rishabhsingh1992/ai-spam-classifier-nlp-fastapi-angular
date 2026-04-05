# TASKS

## Backend

- [x] Create `main.py` entry point with FastAPI app instance and CORS configuration
- [x] Add `.env.example` with all required environment variable keys
- [x] Implement `POST /classify` endpoint — accepts message text, returns `{ label: "spam" | "ham", confidence: number }`
- [x] Integrate AI/ML classification model or external API (e.g., OpenAI, Anthropic, or a local model)
- [x] Add email-specific classification endpoint `POST /classify/email` accepting subject + body
- [x] Add request validation with Pydantic schemas
- [ ] Add rate limiting to classification endpoints

## Frontend

- [x] Create `ClassifyComponent` — text input form with submit button
- [x] Create `ResultComponent` — displays classification label and confidence score
- [x] Create `HistoryComponent` — lists past classification results in session
- [x] Set up `ApiService` to communicate with the FastAPI backend (`POST /classify`)
- [x] Define app routes (`/` → classify form, `/history` → history view)
- [x] Add loading state and error handling to classification form
- [x] Style all components with Tailwind CSS
