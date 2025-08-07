from wagtailsvg.models import Svg
from wagtail import VERSION as WAGTAIL_VERSION
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from wagtail.admin.widgets import BaseChooser
from django.core.exceptions import ObjectDoesNotExist
from django.forms import HiddenInput
from django.urls import reverse
from wagtail.admin.widgets import BaseChooserAdapter
from wagtail.telepath import register
from django import forms


class AdminSvgChooser(BaseChooser):
    choose_one_text = _("Choose an SVG")
    choose_another_text = _("Choose another SVG")
    link_to_chosen_text = _("Edit this SVG")
    model = Svg
    choose_modal_url_name = "wagtailsvg_chooser:choose"
    chooser_modal_url_name = "wagtailsvg_chooser:choose"
    edit_item_url_name = "wagtailsvg:edit"
    clear_choice_text = _("Clear choice")
    template_name = "wagtailsvg/widgets/chooser.html"
    icon = "doc-empty-inverse"
    classname = "svg-chooser"
    js_constructor = "Chooser"

    def get_value_data(self, value):
        # Skip debug output for telepath initialization calls
        if value is None and hasattr(self, "_is_telepath_init"):
            return {
                "value": "",
                "title": "",
                "edit_item_url": None,
                "preview_url": None,
            }

        # Only show debug output when we have an actual value (not None from initialization)
        if value is not None:
            print("🔍 [SVG] get_value_data called with:", value, type(value))

        # Handle the case where value is the string "undefined"
        if value == "undefined":
            if value is not None:
                print("🔍 [SVG] get_value_data: handling 'undefined' string")
            value = None

        if value is None:
            if value is not None:
                print("🔍 [SVG] get_value_data: value is None")
            instance = None
        elif self.model and isinstance(value, self.model):
            print("🔍 [SVG] get_value_data: value is model instance, converting to pk")
            instance = value
            value = value.pk
        else:
            if value is not None:
                print(
                    "🔍 [SVG] get_value_data: trying to get instance for value:", value
                )
            try:
                instance = self.get_instance(value)
            except (
                ObjectDoesNotExist if self.model is None else self.model.DoesNotExist
            ):
                instance = None

        if value is not None:
            print("🔍 [SVG] get_value_data: final value:", value, "instance:", instance)
        if instance is None:
            result = {
                "value": "",
                "title": "",
                "edit_item_url": None,
                "preview_url": None,
            }
        else:
            result = {
                "value": value,
                "title": self.get_title(instance),
                "edit_item_url": self.get_edit_item_url(instance),
                "preview_url": instance.url,
            }

        if value is not None:
            print("🔍 [SVG] get_value_data: returning result:", result)
        return result

    def get_title(self, instance):
        """
        Return the title/display name for the given instance.
        """
        if hasattr(instance, "title") and instance.title:
            return instance.title
        elif hasattr(instance, "filename") and instance.filename:
            return instance.filename
        else:
            return str(instance)

    def render_input_html(self, name, value, attrs):
        """
        Render the hidden input field that contains the actual value.
        """
        input_widget = HiddenInput()
        return input_widget.render(name, value, attrs)

    def value_from_datadict(self, data, files, name):
        """
        Extract the value from form data, converting 'undefined' to None.
        """
        value = data.get(name)

        # Handle empty/undefined values
        if value in ("", "undefined", None):
            return None

        # If it's already an integer, return it
        if isinstance(value, int):
            return value

        # Try to convert to integer (SVG ID)
        try:
            return int(value)
        except (ValueError, TypeError):
            return None

    def get_edit_item_url(self, instance):
        """
        Return the URL for editing the given SVG item.
        """
        try:
            return reverse("wagtailsvg:edit", args=[instance.pk])
        except:
            # If the URL doesn't exist, return None
            return None

    def get_create_item_url(self):
        """
        Return the URL for creating a new SVG item.
        """
        try:
            return reverse("wagtailsvg:create")
        except:
            # If the URL doesn't exist, return None
            return None

    def get_chooser_modal_url(self):
        """
        Return the URL for the chooser modal.
        """
        try:
            return reverse("wagtailsvg_chooser:choose")
        except:
            return None

    def get_instance(self, value):
        """
        Get the model instance for the given value.
        """
        if value is None:
            return None
        try:
            instance = self.model.objects.get(pk=value)
            return instance
        except self.model.DoesNotExist:
            return None

    def render_html(self, name, value, attrs):
        # Skip debug output for telepath initialization calls
        if name in ["__NAME__"]:
            # This is a telepath initialization call, skip debug output
            if value == "undefined":
                value = None

            if (
                WAGTAIL_VERSION >= (6, 0)
                and isinstance(value, dict)
                and "value" in value
            ):
                value_data = value
            else:
                value_data = self.get_value_data(value)

            actual_value = value_data["value"]
            original_field_html = self.render_input_html(name, actual_value, attrs)

            new_field_html = render_to_string(
                self.template_name,
                {
                    "widget": self,
                    "original_field_html": original_field_html,
                    "attrs": attrs,
                    "value": actual_value,
                    "display_title": value_data["title"],
                    "edit_url": value_data["edit_item_url"],
                    "chooser_url": self.get_chooser_modal_url(),
                    "preview_url": value_data["preview_url"],
                },
            )
            return new_field_html

        # Handle the case where value is the string "undefined"
        if value == "undefined":
            value = None

        # In Wagtail 6.0+, value might already be processed value_data dict
        # In older versions, value is the raw value that needs processing
        if WAGTAIL_VERSION >= (6, 0) and isinstance(value, dict) and "value" in value:
            # Already processed value_data from parent render method
            value_data = value
        else:
            # Raw value that needs processing
            value_data = self.get_value_data(value)

        # Keep the original value for the hidden field to preserve state
        # Don't convert empty string to None as this causes state loss
        actual_value = value_data["value"]
        print(
            "🔍 [SVG] render_html: actual_value for hidden field:",
            actual_value,
            type(actual_value),
        )
        original_field_html = self.render_input_html(name, actual_value, attrs)
        print("🔍 [SVG] render_html: original_field_html:", original_field_html)

        new_field_html = render_to_string(
            self.template_name,
            {
                "widget": self,
                "original_field_html": original_field_html,
                "attrs": attrs,
                "value": actual_value,  # The actual value for the hidden field
                "display_title": value_data["title"],  # What the base template expects
                "edit_url": value_data[
                    "edit_item_url"
                ],  # What the base template expects
                "chooser_url": self.get_chooser_modal_url(),
                "preview_url": value_data["preview_url"],
            },
        )
        return new_field_html

    class Media:
        js = []


class AdminSvgChooserAdapter(BaseChooserAdapter):
    js_constructor = "wagtail.admin.widgets.Chooser"

    def js_args(self, widget):
        return [
            widget.render_html("__NAME__", None, attrs={"id": "__ID__"}),
            widget.id_for_label("__ID__"),
            widget.base_js_init_options,
        ]

    class Media:
        js = ["wagtailadmin/js/chooser-widget-telepath.js"]


# Register the widget with Wagtail's telepath system
register(AdminSvgChooserAdapter(), AdminSvgChooser)
