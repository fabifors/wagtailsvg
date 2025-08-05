#!/usr/bin/env python
"""
Simple test script to verify Wagtail 6 compatibility
"""

import sys
import os
import django
from django.conf import settings

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configure Django settings for testing
if not settings.configured:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
    django.setup()


def test_imports():
    """Test that all imports work correctly"""
    print("Testing imports...")

    try:
        from wagtailsvg.models import Svg

        print("✓ Svg model imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import Svg model: {e}")
        return False

    try:
        from wagtailsvg.blocks import SvgChooserBlock

        print("✓ SvgChooserBlock imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import SvgChooserBlock: {e}")
        return False

    try:
        from wagtailsvg.edit_handlers import SvgChooserPanel

        print("✓ SvgChooserPanel imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import SvgChooserPanel: {e}")
        return False

    try:
        from wagtailsvg.widgets import AdminSvgChooser

        print("✓ AdminSvgChooser imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import AdminSvgChooser: {e}")
        return False

    try:
        from wagtailsvg.views import SvgChooserViewSet

        print("✓ SvgChooserViewSet imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import SvgChooserViewSet: {e}")
        return False

    return True


def test_wagtail_imports():
    """Test that Wagtail 6 imports work"""
    print("\nTesting Wagtail 6 imports...")

    try:
        from wagtail.admin.panels import FieldPanel

        print("✓ FieldPanel imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import FieldPanel: {e}")
        return False

    try:
        from wagtail.models import CollectionMember

        print("✓ CollectionMember imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import CollectionMember: {e}")
        return False

    try:
        from wagtail.blocks import ChooserBlock

        print("✓ ChooserBlock imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import ChooserBlock: {e}")
        return False

    return True


def main():
    print("Testing Wagtail 6 compatibility for wagtailsvg...")
    print("=" * 50)

    success = True

    if not test_wagtail_imports():
        success = False

    if not test_imports():
        success = False

    print("\n" + "=" * 50)
    if success:
        print("✓ All tests passed! The package should be compatible with Wagtail 6.")
    else:
        print("✗ Some tests failed. Please check the errors above.")

    return success


if __name__ == "__main__":
    main()
