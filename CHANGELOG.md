# Changelog

All notable changes to F1 Engineering Lab are documented here.
Format: `[version] — date — what changed and why`

---

## [0.1.0] — 2025-06-17 — Project Foundation

### Added
- Monorepo structure: `backend/`, `frontend/`, `ml/`, `docs/`, `infra/`
- FastAPI application skeleton (`main.py`)
- `/cars` router — GET all, GET by ID, POST, DELETE
- `/drivers` router — GET all, GET by ID, POST
- `/tracks` router — GET all, GET by ID, POST
- `/health` endpoint for uptime monitoring
- Pydantic models: `Car`, `CarComponent`, `Driver`, `Track`
- In-memory data store with 3 cars, 4 drivers, 5 tracks
- Input validation via Pydantic `Field()` constraints
- Auto-generated API docs at `/docs`

### Architecture Decisions
- Used in-memory dict store intentionally — database comes in v0.2.0
- Router-per-domain pattern chosen for scalability
- Pydantic chosen over dataclasses for runtime validation

### What I Learned
- FastAPI router pattern — how to split endpoints by domain
- Pydantic BaseModel — runtime type validation vs TypeScript's compile-time only
- HTTP status codes — 201 Created, 204 No Content, 404, 409 Conflict
- Python virtual environments — equivalent of node_modules isolation
- `@router.get`, `@router.post`, `@router.delete` decorators

---

## [Unreleased] — upcoming

### Planned for v0.2.0
- PostgreSQL database integration
- SQLAlchemy ORM models
- Alembic migrations
- Replace in-memory store with real DB queries