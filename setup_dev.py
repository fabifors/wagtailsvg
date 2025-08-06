#!/usr/bin/env python
"""
Setup script for wagtailsvg development environment
This script installs the app in development mode and sets up the database.
"""

import os
import sys
import subprocess
import django
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Command: {command}")
        print(f"   Error: {e.stderr}")
        return False


def main():
    """Set up the development environment."""
    print("🚀 Setting up wagtailsvg development environment...")
    print("=" * 50)

    # Check if we're in the right directory
    if not Path("setup.py").exists():
        print("❌ Error: Please run this script from the wagtailsvg root directory")
        sys.exit(1)

    # Install development requirements
    if not run_command(
        "pip install -r dev_requirements.txt", "Installing development requirements"
    ):
        print("⚠️  Some development tools failed to install, but continuing...")

    # Install the app in development mode
    if not run_command("pip install -e .", "Installing wagtailsvg in development mode"):
        print("❌ Failed to install wagtailsvg in development mode")
        sys.exit(1)

    # Set up Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
    django.setup()

    # Run migrations
    if not run_command("python manage.py migrate", "Running database migrations"):
        print("❌ Failed to run migrations")
        sys.exit(1)

    # Create a superuser if it doesn't exist
    print("🔄 Creating superuser (if needed)...")
    try:
        from django.contrib.auth import get_user_model

        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            print("📝 Creating superuser...")
            print("   Username: admin")
            print("   Email: admin@example.com")
            print("   Password: admin123")

            # Create superuser non-interactively
            user = User.objects.create_superuser(
                username="admin", email="admin@example.com", password="admin123"
            )
            print("✅ Superuser created successfully")
        else:
            print("✅ Superuser already exists")
    except Exception as e:
        print(f"⚠️  Could not create superuser: {e}")

    print("=" * 50)
    print("🎉 Development environment setup complete!")
    print("")
    print("📋 Next steps:")
    print("   1. Run: python dev_server.py")
    print("   2. Open: http://localhost:8000/admin/")
    print("   3. Login with: admin / admin123")
    print("   4. Start developing! Changes will auto-reload.")
    print("")
    print("💡 Development tips:")
    print("   - Your app is installed in development mode")
    print("   - Changes to Python files will auto-reload")
    print("   - Use Django Debug Toolbar for debugging")
    print("   - Check the console for errors and warnings")


if __name__ == "__main__":
    main()
