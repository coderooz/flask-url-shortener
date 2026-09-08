# Project Reference Index

**Reference Metadata:**
```yaml
name: PROJECT_REFERENCE_INDEX
version: 1.0
status: active
last_verified: 2026-09-08
verification_scope: full
```

---

## 1. Project Identity

**Name:** Flask URL Shortener
**Repository:** https://github.com/codeerooz/flask-url-shortener.git
**Branch:** master
**Author:** Ranit Saha (Coderooz)
**License:** MIT
**Category:** Web Application (URL Shortening Service)

---

## 2. Technology Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.12 |
| Framework | Flask |
| Templating | Jinja2 |
| Frontend | HTML5, CSS3 |
| Database | In-memory (dict) — no persistence |
| Packaging | pip + requirements.txt |
| VCS | Git |

---

## 3. Root Structure

```
url-shortner/
├── .git/                    # Git repository data
├── .gitignore               # Git ignore rules
├── .opencode/               # OpenCode governance (PRI)
│   └── reference/
│       └── PROJECT_REFERENCE_INDEX.md
├── .workspace/              # Development artifacts (gitignored)
├── __pycache__/             # Python bytecode (gitignored after fix)
├── .venv/                   # Python virtual environment (gitignored)
├── app.py                   # Main Flask application
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── static/                  # Static assets
│   └── style.css            # Application styles
└── templates/               # Jinja2 templates
    └── index.html           # Home page template
```

---

## 4. Directory Reference

### `static/`

**Type:** Static assets directory
**Purpose:** Contains CSS stylesheets and other static files served by Flask.
**Responsibilities:**
- CSS styling for the web interface
**Contains:**
- `style.css` — main stylesheet

### `templates/`

**Type:** Jinja2 template directory
**Purpose:** Contains HTML templates rendered by Flask.
**Responsibilities:**
- Home page rendering with URL shortening form
**Contains:**
- `index.html` — home page with shortener form

### `.opencode/reference/`

**Type:** Project Reference Index directory
**Purpose:** Houses the canonical PRI for OpenCode navigation.
**Responsibilities:**
- Structural reference for AI agents and developers
**Contains:**
- `PROJECT_REFERENCE_INDEX.md` — this file

### `.workspace/`

**Type:** Development artifact directory (gitignored)
**Purpose:** Temporary working files, reports, session artifacts.
**Responsibilities:**
- Isolated space for non-committed development artifacts

---

## 5. File Reference

### `app.py`

**Type:** Flask application entry point
**Purpose:** Main application file containing all routes and logic.
**Responsibilities:**
- Home page route (`/` and `/home`)
- URL shortening route (`/shorten` — POST)
- Redirect route (`/<short_key>` — GET)
- In-memory URL mapping storage
**Dependencies:**
- `flask` — web framework
- `hashlib` — MD5 hashing for short keys
- `templates/index.html` — home page template
- `static/style.css` — stylesheet
**Layer:** Application / Entry Point

### `requirements.txt`

**Type:** Python dependency manifest
**Purpose:** Lists required Python packages.
**Contains:**
- `Flask` — web framework (actively used)
- `db-sqlite3` — SQLite3 adapter (listed, not currently used)
- `Flask-SQLAlchemy` — SQLAlchemy integration (listed, not currently used)

### `README.md`

**Type:** Project documentation
**Purpose:** Overview, setup instructions, and usage guide.
**Contents:**
- Feature description
- Prerequisites
- Setup instructions
- Running instructions
- How it works
- Future integrations
- License reference
- Author info

### `static/style.css`

**Type:** CSS stylesheet
**Purpose:** Visual styling for the URL shortener web interface.
**Responsibilities:**
- Centered layout
- Form styling
- Typography

### `templates/index.html`

**Type:** Jinja2 HTML template
**Purpose:** Home page with URL shortening form.
**Responsibilities:**
- Display URL input form
- Show shortened URL after submission
**Route:** `/` and `/home`

---

## 6. Application Routes

| Route | Method | Purpose | Handler |
|-------|--------|---------|---------|
| `/` | GET | Home page with form | `index()` |
| `/home` | GET | Home page (alias) | `index()` |
| `/shorten` | POST | Shorten a URL | `shorten()` |
| `/<short_key>` | GET | Redirect to original URL | `redirect_to_url()` |

### Route Details

**`/` and `/home`**
- Filesystem: `app.py` — `index()` function
- Template: `templates/index.html`
- Purpose: Displays the URL shortening form

**`/shorten`**
- Filesystem: `app.py` — `shorten()` function
- Method: POST
- Accepts: `url` form field
- Behavior: Generates MD5-based short key, stores mapping, redirects to home with result

**`/<short_key>`**
- Filesystem: `app.py` — `redirect_to_url()` function
- Parameter: `short_key` (6-char MD5 prefix)
- Behavior: Looks up original URL in memory, redirects or returns 404

---

## 7. Configuration

### `requirements.txt`

**Purpose:** Python package dependencies.
**Important note:** `db-sqlite3` and `Flask-SQLAlchemy` are listed but NOT used in the current codebase. They appear to be for future database integration.

### `.gitignore`

**Purpose:** Git ignore rules for Python project.
**Current coverage:**
- `.venv` — virtual environment
- `__pycache__/` — bytecode
- `*.py[cod]` — compiled Python
- `.workspace/` — OpenCode artifacts
- `.opencode/` — OpenCode config
- MCP runtime files

---

## 8. Scripts & Commands

| Command | Purpose |
|---------|---------|
| `python app.py` | Run the Flask development server |
| `pip install -r requirements.txt` | Install dependencies |
| `python -m venv venv` | Create virtual environment |

---

## 9. Architectural Relationships

```
User Request
    ↓
Flask Router (app.py)
    ↓
Route Handler
    ↓
┌─────────────────────────┐
│ In-Memory url_map (dict) │
│ (not persistent)         │
└─────────────────────────┘
    ↓
Template Rendering (templates/index.html)
    ↓
Static Assets (static/style.css)
    ↓
HTTP Response to Browser
```

---

## 10. Important Entry Points

| Entry Point | File | Purpose |
|------------|------|---------|
| Application | `app.py` | Main Flask app, routes, logic |
| Template | `templates/index.html` | Home page UI |
| Styles | `static/style.css` | Visual styling |
| Dependencies | `requirements.txt` | Package requirements |

---

## 11. Project-Specific Conventions

- **In-memory storage:** URL mappings stored in Python dict (lost on restart)
- **Short key generation:** MD5 hash of original URL, truncated to 6 characters
- **Template rendering:** Jinja2 with `render_template()`
- **Redirect pattern:** `request.host_url + short_key` for full short URL

---

## 12. Known Limitations

- No persistent storage (in-memory only)
- No user authentication
- No custom short keys
- No URL validation
- No analytics/tracking
- `db-sqlite3` and `Flask-SQLAlchemy` dependencies listed but unused

---

## 13. Reference Maintenance Log

### 2026-09-08
- **Change:** Initial PRI creation
- **Classification:** ADDED
- **Verification:** FULL
- **Updated sections:** All (initial creation)
