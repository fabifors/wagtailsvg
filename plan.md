# SVG Chooser Block Fix Plan

## Problem Description

The SVG chooser block allows selecting an SVG file and saving it once, but when saving again, the SVG is removed from the page as if it was left blank. This suggests the JavaScript/code doesn't maintain the previous file context after page reload.

## Investigation Steps

1. **Analyze the current codebase structure** - Understand how the SVG chooser block works
2. **Examine the widget implementation** - Check the AdminSvgChooser widget for state management issues
3. **Review form state handling** - Investigate how form state is preserved between saves
4. **Check JavaScript functionality** - Look for client-side code that might be clearing the selection
5. **Test the current behavior** - Run the application to reproduce the issue
6. **Identify the root cause** - Determine why the SVG selection is lost on subsequent saves
7. **Implement the fix** - Apply the necessary changes to maintain state
8. **Test the fix** - Verify the issue is resolved

## Current Status

- [x] Initial investigation started
- [x] Root cause identified
- [x] Fix implemented
- [x] Testing completed

## Findings

1. **Widget State Issue**: The `render_html` method in `AdminSvgChooser` converts empty string values to `None`, which may cause the widget to lose its state on subsequent saves.

2. **Message Type Mismatch**: The chooser templates are using a custom message type `'svg_chooser:choose'` but Wagtail's standard chooser expects a different message format.

3. **Value Data Handling**: The `get_value_data` method returns empty string for "value" when instance is None, but `render_html` converts this to `None`, potentially causing state loss.

4. **Debug Logging**: There's already debug logging in place that shows the issue - the `value_from_datadict` method is being called and should help identify when values are being lost.

5. **CRITICAL: Block Form State Issue**: The `SvgChooserBlock.get_form_state` method was returning a processed value_data dictionary instead of the raw value (SVG ID). This caused StreamFields to lose the SVG selection on re-save because the widget expected the raw ID value, not a processed dictionary.

## Solution

1. **Fixed Widget State Issue**: Removed the conversion of empty string to `None` in the `render_html` method. The widget now preserves the original value from `get_value_data` to maintain state between saves.

2. **Fixed Message Type Mismatch**: Updated the chooser templates to use the standard Wagtail message type `'chooser:choose'` instead of the custom `'svg_chooser:choose'` type.

3. **Improved Debug Logging**: Enhanced the debug logging in both `get_value_data` and `value_from_datadict` methods to better track state changes.

4. **Fixed URL References**: Updated the chooser templates to use the correct URL namespace `'wagtailsvg:edit'` instead of `'svg_chooser:edit'`.

5. **Fixed Template Inheritance**: Updated chooser templates to properly extend Wagtail's base chooser templates (`wagtailadmin/generic/chooser/choose.html` and `wagtailadmin/generic/chooser/results.html`).

6. **Switched to Standard Chooser Interface**: Disabled custom chooser templates and switched to using Wagtail's standard chooser interface, which handles JavaScript communication properly.

7. **Fixed JavaScript Constructor**: Updated the widget's `js_constructor` to use the standard Wagtail chooser constructor.

8. **Added Missing Methods**: Added `get_instance` and `get_chooser_modal_url` methods to ensure proper widget functionality.

9. **Enhanced Block Value Handling**: Added `value_from_form` method to the block to properly handle form value conversion.

10. **CRITICAL FIX: Fixed Block Form State**: Fixed the `get_form_state` method to return the raw SVG ID instead of a processed value_data dictionary. This was the root cause of the StreamField state loss issue.

11. **Enhanced Error Handling**: Added proper error handling in `get_form_state` to handle various input types (None, empty string, invalid values) gracefully.

12. **Added Database Value Conversion**: Added `to_python`, `get_prep_value`, and `get_db_prep_value` methods to ensure proper value conversion during database operations.

The root cause was that the widget was converting empty string values to `None` in the `render_html` method, which caused the widget to lose its state on subsequent saves. Additionally, the chooser templates were not properly extending the base Wagtail chooser templates, which could cause JavaScript communication issues. Most critically, the `SvgChooserBlock.get_form_state` method was returning a processed dictionary instead of the raw value, causing StreamFields to lose SVG selections on re-save. By preserving the original value, fixing the message type, ensuring proper template inheritance, and fixing the block's form state handling, the chooser should now maintain its state correctly.
