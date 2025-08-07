from django.db import models

try:
    from wagtail.fields import StreamField
    from wagtail.models import Page
    from wagtail.admin.panels import FieldPanel as StreamFieldPanel
except ImportError:
    from wagtail.core.fields import StreamField
    from wagtail.core.models import Page
    from wagtail.admin.edit_handlers import StreamFieldPanel

from wagtailsvg.blocks import SvgChooserBlock
from .blocks import TextBlock


# =================================
# TestPage used for testing purpose
# =================================


class TestPage(Page):
    body = StreamField(
        [
            ("text", TextBlock()),
            ("svg", SvgChooserBlock()),
        ],
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]
