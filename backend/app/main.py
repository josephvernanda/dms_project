from fastapi import FastAPI
from app.api import auth, documents, permissions, notifications


app = FastAPI(
    title="DMS - Document Management System API",
    description="""
## Document Management System API

This API allows users to:

- Register & Login
- Upload Documents
- Replace Documents (with permission)
- Delete Documents (with approval)
- Receive Notifications

### Tech Stack
- FastAPI
- SQLAlchemy
- JWT Authentication
- SQLite (Development)
""",
    version="1.0.0",
    contact={
        "name": "Joseph Vernanda",
        "email": "joseph@email.com",
    },
    docs_url="/swagger",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.include_router(auth.router)
app.include_router(documents.router)
app.include_router(permissions.router)
app.include_router(notifications.router)