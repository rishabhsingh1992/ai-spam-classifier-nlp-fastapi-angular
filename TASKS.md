# TASKS

## Backend

- [ ] Create `main.py` entry point with FastAPI app instance and CORS configuration
- [ ] Add `.env.example` with all required environment variable keys
- [ ] Implement `POST /classify` endpoint — accepts message text, returns `{ label: "spam" | "ham", confidence: number }`
- [ ] Integrate AI/ML classification model or external API (e.g., OpenAI, Anthropic, or a local model)
- [ ] Add email-specific classification endpoint `POST /classify/email` accepting subject + body
- [ ] Add request validation with Pydantic schemas
- [ ] Add rate limiting to classification endpoints

## Frontend

- [ ] Create `ClassifyComponent` — text input form with submit button
- [ ] Create `ResultComponent` — displays classification label and confidence score
- [ ] Create `HistoryComponent` — lists past classification results in session
- [ ] Set up `ApiService` to communicate with the FastAPI backend (`POST /classify`)
- [ ] Define app routes (`/` → classify form, `/history` → history view)
- [ ] Add loading state and error handling to classification form
- [ ] Style all components with Tailwind CSS
