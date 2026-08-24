# AI Shorts Factory

Local-first AI short-form video production platform.

Build YouTube Shorts, Instagram Reels, and Facebook Reels with AI-powered content generation.

## Features (In Development)

- **Local-first**: Run entirely on your machine
- **Modular architecture**: Provider-agnostic design
- **Content pipeline**: Idea → Plan → Research → Script → Scenes → Voice → Video → Publish
- **Versioning**: Track all changes to projects and assets
- **Quality control**: Built-in validation and review workflows
- **Job system**: Resumable, fault-tolerant long-running tasks
- **Multiple platforms**: YouTube Shorts, Instagram Reels, Facebook Reels

## Requirements

- Python 3.13+
- FFmpeg (for video rendering)
- SQLite (included in Python)
- Optional: Ollama (for local LLM), Google Gemini API (for cloud LLM)

## Quick Start

### 1. Setup

```bash
python setup.ps1  # Windows
# or
bash setup.sh     # Linux/macOS
```

### 2. Configure

Create `.env` from `.env.example`:

```bash
cp .env.example .env
```

### 3. Run

```bash
python -m uvicorn app.main:app --reload
```

API will be available at `http://127.0.0.1:8000`

OpenAPI docs: `http://127.0.0.1:8000/docs`

## Development Phases

- [x] **Phase 1**: Backend foundation, config, logging, health
- [ ] **Phase 2**: Database, models, repositories
- [ ] **Phase 3**: LLM abstraction, providers
- [ ] **Phase 4**: Content planner
- [ ] **Phase 5**: Research, fact-checking
- [ ] **Phase 6**: Script generation, scenes
- [ ] **Phase 7**: Text-to-speech
- [ ] **Phase 8**: Captions
- [ ] **Phase 9**: Video generation
- [ ] **Phase 10**: FFmpeg rendering
- [ ] **Phase 11**: Quality control
- [ ] **Phase 12**: Job system
- [ ] **Phase 13**: Library, history, versioning
- [ ] **Phase 14-20**: Publishing, analytics, frontend

## API Health Check

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/health/providers
```

## Project Structure

```
app/
  main.py              # FastAPI application
  core/                # Configuration, logging, exceptions
  api/                 # API routes
  db/                  # Database models and repositories
  schemas/             # Pydantic models
  services/            # Business logic
  providers/           # External API integrations
  jobs/                # Job queue system
  media/               # Media processing
  utils/               # Utilities

tests/                 # Test suite
docs/                  # Documentation
data/                  # Local data (projects, logs, temp files)
```

## Configuration

All settings are configured via environment variables (see `.env.example`).

### Key Settings

- `LLM_PROVIDER`: `mock`, `gemini`, `ollama`
- `TTS_PROVIDER`: `mock`, `google`, `elevenlabs`
- `VIDEO_PROVIDER`: `mock`, `runwayml`
- `OFFLINE_MODE`: Set to `true` for development without external APIs

## Documentation

- [Architecture](docs/architecture.md)
- [Setup](docs/setup.md)
- [Configuration](docs/configuration.md)
- [Providers](docs/providers.md)
- [API](docs/api.md)

## License

MIT
