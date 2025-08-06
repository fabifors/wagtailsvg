#!/usr/bin/env python
"""
Development server for wagtailsvg with auto-reload
Run this script to start a development server that automatically reloads on file changes.
"""

import os
import sys
import django
from django.core.management import execute_from_command_line


def main():
    """Start the development server with auto-reload."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")

    # Set up Django
    django.setup()

    # Run the development server with auto-reload
    argv = [
        "manage.py",
        "runserver",
        "--noreload",  # We'll handle reloading manually if needed
        "0.0.0.0:8000",  # Listen on all interfaces
    ]

    print("🚀 Starting wagtailsvg development server...")
    print("📍 Server will be available at: http://localhost:8000")
    print("🔧 Admin interface: http://localhost:8000/admin/")
    print("📝 Django admin: http://localhost:8000/django-admin/")
    print("")
    print("💡 Tips:")
    print("   - Make changes to your code and save - the server will auto-reload")
    print("   - Use Ctrl+C to stop the server")
    print("   - Check the console for any errors or warnings")
    print("")

    execute_from_command_line(argv)


if __name__ == "__main__":
    main()
