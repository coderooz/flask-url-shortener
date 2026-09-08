# Developer Notes

Technical documentation for developers working on or extending this project.

## Architecture Overview

```
User → Browser → Flask (app.py) → In-Memory Store (dict) → Response
```

The application follows a simple monolithic architecture with no database persistence.

## Application Flow

### 1. Home Page (`/` or `/home`)

```python
@app.route("/")
def index():
    return render_template("index.html")
```

- Renders the URL shortening form
- Displays shortened URL if present in `short_url` query parameter

### 2. Shorten URL (`/shorten` — POST)

```python
@app.route("/shorten", methods=["POST"])
def shorten():
    original_url = request.form["url"]
    short_key = hashlib.md5(original_url.encode()).hexdigest()[:6]
    url_map[short_key] = original_url
    short_url = request.host_url + short_key
    return redirect(url_for("index", short_url=short_url))
```

- Receives URL from form submission
- Generates 6-character MD5 hash as short key
- Stores mapping in `url_map` dictionary
- Redirects to home page with shortened URL

### 3. Redirect (`/<short_key>` — GET)

```python
@app.route("/<short_key>")
def redirect_to_url(short_key):
    original_url = url_map.get(short_key)
    if original_url:
        return redirect(original_url)
    else:
        return "URL not found", 404
```

- Looks up short key in `url_map`
- Redirects to original URL or returns 404

## Data Model

```python
url_map = {
    "a1b2c3": "https://example.com",
    "d4e5f6": "https://another.com"
}
```

- In-memory dictionary
- Keys: 6-character MD5 hash prefixes
- Values: Original URLs
- **NOT PERSISTENT** — lost on server restart

## Key Functions

| Function | Purpose | Input | Output |
|----------|---------|-------|--------|
| `index()` | Render home page | None | HTML response |
| `shorten()` | Create short URL | `url` form field | Redirect |
| `redirect_to_url()` | Redirect to original | `short_key` path param | Redirect/404 |

## Dependencies

### Active

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.x | Web framework |

### Listed but Unused

| Package | Purpose |
|---------|---------|
| db-sqlite3 | SQLite3 database adapter |
| Flask-SQLAlchemy | SQLAlchemy ORM integration |

These are intended for future database persistence.

## Template Structure

### `templates/index.html`

- Form with `POST` action to `/shorten`
- Input field for URL submission
- Conditional display of shortened URL
- Links to static stylesheet

### `static/style.css`

- Centered container layout
- Form styling
- Typography definitions

## Extending the Application

### Adding Database Persistence

1. Uncomment/add SQLAlchemy imports
2. Define `URL` model
3. Replace `url_map` dict operations with DB queries
4. Add `db.init_app(app)` and `db.create_all()`

### Adding Custom Short Keys

1. Add validation for custom key input
2. Check for key collisions
3. Store user-provided key instead of hash

### Adding URL Validation

1. Add `validators` library to requirements
2. Validate URL format before processing
3. Return error for invalid URLs

### Adding Analytics

1. Add click count to URL model
2. Increment on each redirect
3. Add analytics page/route

## Environment Variables

Currently none required. For future use:

```bash
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///urls.db
```

## Testing

```bash
# Run the app
python app.py

# Test manually in browser
# http://127.0.0.1:5000/

# Test URL shortening
# Enter a URL and verify redirect works
```

## Known Issues

1. No persistent storage — data lost on restart
2. No input validation on URLs
3. No rate limiting
4. MD5 hashes can have collisions (low probability for URL shortening)

## Future Improvements

- [ ] SQLite/PostgreSQL database integration
- [ ] User authentication
- [ ] Custom short keys
- [ ] URL validation
- [ ] Click analytics
- [ ] API endpoints
- [ ] Rate limiting
- [ ] Expiration dates for URLs
