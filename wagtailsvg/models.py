import os
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from wagtail.search import index
from wagtail.models import CollectionMember
from wagtail.admin.panels import TabbedInterface, ObjectList, FieldPanel

from taggit.managers import TaggableManager


def get_svg_upload_to_folder(instance, filename):
    folder = settings.WAGTAILSVG_UPLOAD_FOLDER or "media"
    return os.path.join(folder, filename)


class Svg(CollectionMember, index.Indexed, models.Model):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    file = models.FileField(upload_to=get_svg_upload_to_folder, verbose_name=_("file"))
    tags = TaggableManager(help_text=None, blank=True, verbose_name=_("tags"))

    class Meta:
        ordering = ["-id"]

    admin_form_fields = (
        "title",
        "file",
        "collection",
        "tags",
    )

    panels = [
        FieldPanel("collection"),
        FieldPanel("title"),
        FieldPanel("file"),
        FieldPanel("tags"),
    ]

    def __str__(self):
        return self.title

    @property
    def filename(self):
        return os.path.basename(self.file.name)

    @property
    def url(self):
        return self.file.url

    def get_svg_content(self):
        """Get the SVG content as a string for preview purposes."""
        try:
            if self.file:
                with self.file.open("r") as f:
                    return f.read().decode("utf-8")
        except (UnicodeDecodeError, IOError):
            return None
        return None

    def get_svg_dimensions(self):
        """Get SVG width and height from the content."""
        content = self.get_svg_content()
        if content:
            import re

            width_match = re.search(r'width=["\']([^"\']+)["\']', content)
            height_match = re.search(r'height=["\']([^"\']+)["\']', content)
            viewbox_match = re.search(r'viewBox=["\']([^"\']+)["\']', content)

            width = width_match.group(1) if width_match else None
            height = height_match.group(1) if height_match else None
            viewbox = viewbox_match.group(1) if viewbox_match else None

            return {"width": width, "height": height, "viewbox": viewbox}
        return None
