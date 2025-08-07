from django.utils.functional import cached_property
from django.utils.html import format_html
from wagtail.blocks import ChooserBlock


class SvgChooserBlock(ChooserBlock):

    @cached_property
    def target_model(self):
        from wagtailsvg.models import Svg

        return Svg

    @cached_property
    def widget(self):
        from wagtailsvg.widgets import AdminSvgChooser

        return AdminSvgChooser()

    def get_form_state(self, value):
        """
        Return the value in a form-compatible format.
        This ensures the block properly handles the form state.
        """
        # Only show debug output when we have an actual SVG value
        if value is not None and hasattr(value, "pk"):
            print("\n" + "=" * 60)
            print("🔍 [SVG] get_form_state: value:", value)
            print("=" * 60 + "\n")

        if value is None:
            return None
        elif hasattr(value, "pk"):
            return value.pk
        else:
            return value
