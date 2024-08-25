# Flask URL Shortener

This is a simple URL shortener application built with Flask and Python. It allows users to shorten long URLs and then redirect to the original URLs using a short key.

## Features

- Shorten URLs and redirect to the original URL using a short key.
- Display the shortened URL on the homepage.

## Prerequisites

- Python 3.x
- Flask (installable via pip)

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/coderooz/flask-url-shortener.git
   cd flask-url-shortener
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\Activate.ps1
   ```

3. **Install the required packages**

   ```bash
   pip install flask
   ```

4. **Create the template file**

   Create a file named `index.html` in a folder named `templates` in the same directory as `app.py` with the following content:

   ```html
   <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>URL Shortener</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}"> 
    </head>
    <body>
        <h1>URL Shortener</h1>            
        <form action="/shorten" method="post">
            <label for="url">Enter URL:</label>
            <input type="text" id="url" name="url" required>
            <input type="submit" value="Shorten">
        </form>

        {% if short_url %}
        <p>Short URL: <a target="blank" href="{{ short_url }}">{{ short_url }}</a></p>
    {% endif %} 
    </body>
    </html>
   ```

## Running the Application

1. **Run the Flask application**

   ```bash
   python app.py
   ```

2. **Open your web browser and go to** `http://127.0.0.1:5000/` or `http://localhost:5000/`

   You should see the URL shortener form. Enter a URL and click "Shorten" to get a shortened URL.

## How It Works

- **Homepage (`/`)**: Displays a form where users can enter a URL to shorten. The shortened URL will be displayed on the same page.
- **Shorten URL (`/shorten`)**: Accepts a POST request with the original URL, generates a short key, and stores the mapping in memory.
- **Redirect (`/<short_key>`)**: Redirects to the original URL based on the short key.

## Note

This application uses in-memory storage for URL mappings, which means that all URLs will be lost if the server is restarted. For production use, consider integrating a persistent database.

## Future Integrations

- **Database**
- **Added UI Interface**
- **User Login**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Ranit Saha**

