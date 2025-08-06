# Wagtail SVG Development Guide

This guide explains how to set up and use the development environment for wagtailsvg with live reloading and debugging capabilities.

## Quick Start

1. **Set up the development environment:**

   ```bash
   python setup_dev.py
   ```

2. **Start the development server:**

   ```bash
   python dev_server.py
   ```

3. **Access the application:**
   - Main site: http://localhost:8000
   - Wagtail admin: http://localhost:8000/admin/
   - Django admin: http://localhost:8000/django-admin/
   - Login: `admin` / `admin123`

## Development Features

### 🔄 Auto-Reload

The development server automatically reloads when you make changes to:

- Python files (models, views, etc.)
- Template files
- Static files

### 🐛 Debug Tools

- **Django Debug Toolbar**: Shows SQL queries, request info, and more
- **Django Extensions**: Additional management commands and utilities
- **Auto-reload**: No need to restart the server for most changes

### 📁 File Structure

```
wagtailsvg/
├── wagtailsvg/          # Your app code (live changes)
├── tests/               # Test settings and models
├── manage.py            # Django management
├── dev_server.py        # Development server
├── setup_dev.py         # Development setup
└── dev_requirements.txt # Development dependencies
```

## Development Workflow

1. **Make changes** to your code in the `wagtailsvg/` directory
2. **Save the file** - the server will auto-reload
3. **Test your changes** in the browser
4. **Check the console** for any errors or warnings

## Common Commands

```bash
# Start development server
python dev_server.py

# Run Django management commands
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Run tests
python run_tests.py

# Install in development mode (if needed)
pip install -e .
```

## Debugging Tips

### Using Django Debug Toolbar

1. Install: `pip install django-debug-toolbar`
2. The toolbar will appear on the right side of pages
3. Shows SQL queries, request info, and more

### Using Django Extensions

1. Install: `pip install django-extensions`
2. Additional commands available:
   ```bash
   python manage.py shell_plus  # Enhanced shell
   python manage.py runserver_plus  # Enhanced server
   ```

### Monitoring Changes

- Watch the console output for auto-reload messages
- Check for import errors or syntax issues
- Use browser developer tools for frontend debugging

## Troubleshooting

### Server won't start

- Check if port 8000 is available
- Ensure all dependencies are installed
- Check for syntax errors in your code

### Changes not reloading

- Make sure you're editing files in the `wagtailsvg/` directory
- Check the console for error messages
- Try restarting the server manually

### Database issues

- Run `python manage.py migrate` to apply migrations
- Delete `tests/db.sqlite3` and run setup again if needed

## Production vs Development

This setup is for **development only**. For production:

- Use proper WSGI server (Gunicorn, uWSGI)
- Set `DEBUG = False`
- Use production database (PostgreSQL, MySQL)
- Configure proper static file serving

## Contributing

When making changes:

1. Test your changes thoroughly
2. Run the test suite: `python run_tests.py`
3. Update documentation if needed
4. Follow the existing code style
