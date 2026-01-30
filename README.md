# Pastebin Lite – Django REST API

A simple Pastebin-like backend application built using Django and Django REST Framework.

## Features
- Create text pastes via REST API
- Generate shareable links
- View pastes using unique IDs
- Optional expiry support (time / view-based)
- Clean RESTful API design

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (local)
- Deployed on Render

## API Endpoints

### Create Paste
POST /api/pastes/

Request Body:
{
  "content": "Hello world",
  "max_views": 3
}

Response:
{
  "id": "<uuid>",
  "url": "/api/pastes/<uuid>"
}

### View Paste
GET /api/pastes/<uuid>

Response:
{
  "content": "Hello world",
  "expired": false
}

## Setup Locally
1. Create virtual environment
2. Install dependencies
3. Run migrations
4. Start server

## Notes
This project was built as part of a backend-focused take-home assignment and designed to be compatible with automated testing.
