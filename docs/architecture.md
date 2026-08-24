# AI Shorts Factory - Architecture

## Overview

AI Shorts Factory is a local-first, modular platform for generating short-form video content.

## Design Principles

1. **Local-first**: Run entirely on user's machine
2. **Modular**: Clear separation of concerns
3. **Provider-agnostic**: External services are swappable
4. **Resumable**: Failed jobs can be retried
5. **Fault-tolerant**: System continues operating after errors
6. **Versioned**: All changes are tracked
7. **Testable**: Comprehensive test coverage
8. **Observable**: Rich logging and diagnostics
9. **Secure**: No hardcoded secrets, credentials protected
10. **Deterministic**: Reproducible results where practical

## Architectural Layers

```
┌──────────────────────────────────────┐
│      REST API (FastAPI)         │
├──────────────────────────────────────┤
│   Application Services Layer    │
│  (Project, Script, Video, etc)  │
├──────────────────────────────────────┤
│        Domain Logic Layer       │
│ (Planning, Research, Rendering) │
├──────────────────────────────────────┤
│   Repositories/Data Access      │
│    (SQLAlchemy, SQLModel)       │
├──────────────────────────────────────┤
│  Providers & Infrastructure     │
│ (LLM, TTS, Video, FFmpeg, etc)  │
├──────────────────────────────────────┤
│   Operating System & Cloud APIs │
└──────────────────────────────────────┘
```

## Content Pipeline

```
1. PROJECT CREATION
   ↓
2. TOPIC CLASSIFICATION
   ↓
3. CONTENT PLANNING
   ↓
4. RESEARCH
   ↓
5. FACT CHECKING
   ↓
6. SCRIPT GENERATION
   ↓
7. SCENE GENERATION
   ↓
8. VISUAL GENERATION
   ↓
9. VOICEOVER
   ↓
10. BACKGROUND MUSIC
   ↓
11. CAPTIONS
   ↓
12. VIDEO ASSEMBLY
   ↓
13. THUMBNAIL / COVER
   ↓
14. QUALITY CONTROL
   ↓
15. METADATA
   ↓
16. HUMAN REVIEW
   ↓
17. OPTIONAL PUBLISHING
   ↓
18. ANALYTICS
```

## Provider Architecture

Every external capability is abstracted behind a provider interface:

### LLMProvider
- `generate_text()`
- `generate_structured()`
- `health_check()`

### VideoProvider
- `generate_video()`
- `get_status()`
- `download_result()`

### TTSProvider
- `synthesize_speech()`
- `health_check()`

### ResearchProvider
- `search()`
- `health_check()`

### Publisher
- `authenticate()`
- `upload()`
- `publish()`

Providers can be:
- Mock (for development)
- Local (e.g., Ollama, local FFmpeg)
- Cloud-based (e.g., Google Gemini, ElevenLabs)

## Database Schema

### Core Tables

- `projects`: Content ideas and projects
- `project_versions`: Versioned content
- `scenes`: Video scenes
- `assets`: Generated media files
- `jobs`: Long-running tasks
- `job_events`: Job progress tracking

### Supporting Tables

- `research_sources`: Research materials
- `claims`: Factual claims extracted from scripts
- `fact_checks`: Fact-check results
- `publishing_accounts`: Connected publishing accounts
- `publishing_jobs`: Publishing attempts
- `analytics_events`: Usage analytics

## Job System

Long-running operations become jobs:

- LLM generation
- Research
- Fact-checking
- Video generation
- TTS synthesis
- FFmpeg rendering
- Publishing

Each job:
- Has unique ID
- Tracks progress
- Can be retried
- Can be cancelled
- Stores results and errors
- Maintains detailed logs

## Resumability

The pipeline is designed to resume from any point:

- Completed stages are cached
- Failed stages can be retried
- Users can modify and regenerate specific sections
- No unnecessary reprocessing of successful work

## Configuration

All settings loaded from environment variables via `pydantic-settings`:

- Application: name, environment, debug
- API: host, port, CORS
- Database: connection string
- Storage: directories for projects, temp, logs
- Providers: type, credentials, configuration
- Content: defaults for duration, resolution, language
- Jobs: concurrency limits, timeouts, retries

## Security

- Credentials via environment variables only
- No secrets in logs
- Path validation to prevent traversal
- Safe subprocess handling
- CORS configured for frontend

## Testing

- Unit tests for services and utilities
- Integration tests for database and APIs
- End-to-end tests for complete pipeline
- Mock providers for development

## Performance

- Async/await for I/O operations
- Job queuing prevents blocking
- Caching via content hashing
- Lazy loading of assets
- Streaming for large media files
