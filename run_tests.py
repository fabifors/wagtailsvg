#!/usr/bin/env python
"""
Test runner for wagtailsvg Wagtail 6 compatibility
"""

import os
import sys
import django
from django.conf import settings

if __name__ == "__main__":
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
    django.setup()

    # Run the compatibility test
    print("Running Wagtail 6 compatibility tests...")
    from tests.test_wagtail6_compatibility import main as run_compatibility_tests

    compatibility_success = run_compatibility_tests()

    if compatibility_success:
        print("\n✓ All compatibility tests passed!")
        print("The package is compatible with Wagtail 6.")
    else:
        print("\n✗ Compatibility tests failed.")
        sys.exit(1)
