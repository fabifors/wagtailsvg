# Wagtail 6 Compatibility Changes

This document outlines the changes made to make wagtailsvg compatible with Wagtail 6 while maintaining GPL-3.0 license compliance.

## License Compliance Changes

### 1. Copyright Headers

- Added GPL-3.0 copyright headers to `wagtailsvg/__init__.py`
- Updated version number to indicate this is a modified version (`0.0.39-wagtail6`)

### 2. Package Metadata

- Updated `setup.py` to reflect this is a modified version
- Changed author field to indicate original author and modifications
- Updated description to mention Wagtail 6 compatibility

### 3. Documentation

- Added prominent notice in `README.rst` that this is a modified version
- Included reference to original repository
- Maintained GPL-3.0 license notice

## Wagtail 6 Compatibility Changes

### 1. Import Updates

- Updated imports to use Wagtail 6 module structure:
  - `wagtail.admin.panels` instead of `wagtail.admin.edit_handlers`
  - `wagtail.models` for `CollectionMember`
  - `wagtail.blocks` for `ChooserBlock`

### 2. Dependencies

- Updated `requirements.txt` and `setup.py` to specify:
  - `wagtail>=6.0,<7.0`
  - `django>=4.2,<5.0`

### 3. Model Updates

- Updated `Svg` model to use Wagtail 6 imports
- Maintained compatibility with `CollectionMember` and `index.Indexed`

## Test Organization

### 1. Test Structure

- Moved `test_wagtail6_compatibility.py` from root to `tests/` directory
- Created proper Django test configuration in `tests/settings.py`
- Added `pytest.ini` for test discovery
- Created `run_tests.py` script for easy test execution

### 2. Test Configuration

- Added Django settings for testing with Wagtail 6
- Created URL and WSGI configurations for test environment
- Configured proper test discovery and execution

## Files Modified

### Core Package Files

- `wagtailsvg/__init__.py` - Added GPL headers and version
- `wagtailsvg/models.py` - Updated imports for Wagtail 6
- `wagtailsvg/edit_handlers.py` - Updated imports for Wagtail 6
- `wagtailsvg/blocks.py` - Updated imports for Wagtail 6

### Configuration Files

- `setup.py` - Updated version and metadata
- `requirements.txt` - Updated dependencies
- `README.rst` - Added modification notice

### Test Files

- `tests/test_wagtail6_compatibility.py` - Moved from root
- `tests/settings.py` - New Django test settings
- `tests/urls.py` - New URL configuration
- `tests/wsgi.py` - New WSGI configuration
- `pytest.ini` - Test configuration
- `run_tests.py` - Test runner script

## Running Tests

To run the tests:

```bash
# Run compatibility tests only
python tests/test_wagtail6_compatibility.py

# Run all tests with Django test runner
python run_tests.py

# Run with pytest
pytest tests/
```

## License Compliance

This modified version complies with GPL-3.0 requirements by:

1. **Prominent Modification Notice**: Clearly marked as modified version
2. **Copyright Attribution**: Properly attributed to original author
3. **License Preservation**: Maintained GPL-3.0 license
4. **Source Code Availability**: All modifications are in source code
5. **Version Identification**: Version number indicates modification

## Original Work

- **Original Author**: Alexis Le Baron
- **Original Repository**: https://github.com/Aleksi44/wagtailsvg
- **Original License**: GPL-3.0
- **Modification Date**: 2024
- **Modification Purpose**: Wagtail 6 compatibility
