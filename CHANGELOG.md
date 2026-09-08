# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-01-01

### Added
- Initial release of Flask URL Shortener
- Home page with URL shortening form
- Short URL generation using MD5 hash (6-char prefix)
- In-memory URL storage and retrieval
- Redirect from short URL to original URL
- Basic CSS styling
- 404 error handling for invalid short keys

### Known Limitations
- In-memory storage only (URLs lost on server restart)
- No user authentication
- No custom short keys
- No URL validation
- No analytics or click tracking
