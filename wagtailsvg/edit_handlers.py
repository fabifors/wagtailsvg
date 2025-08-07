from wagtail.admin.panels import FieldPanel
from wagtailsvg.widgets import AdminSvgChooser


class SvgChooserPanel(FieldPanel):
    def __init__(self, field_name, disable_comments=None, permission=None, **kwargs):
        super().__init__(field_name, **kwargs)
        self.widget = AdminSvgChooser()
        self.disable_comments = disable_comments
        self.permission = permission

    def get_form_options(self):
        """
        Return a dict of options to pass to the form constructor.
        """
        options = super().get_form_options()
        options["widgets"] = options.get("widgets", {})
        options["widgets"][self.field_name] = self.widget
        return options
