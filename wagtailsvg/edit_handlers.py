from wagtail.admin.panels import FieldPanel
from wagtailsvg.widgets import AdminSvgChooser


class SvgChooserPanel(FieldPanel):
    def __init__(self, field_name, disable_comments=None, permission=None, **kwargs):
        super().__init__(field_name, **kwargs)
        self.widget = AdminSvgChooser
        self.disable_comments = disable_comments
        self.permission = permission
