import requests
from io import BytesIO
from django.core.files.images import ImageFile

try:
    from wagtail.blocks import RichTextBlock
except ImportError:
    from wagtail.core.blocks import RichTextBlock

from tests import constants


# ===============================
# Blocks used for testing purpose
# ===============================


class TextBlock(RichTextBlock):
    def __init__(self, **kwargs):
        super().__init__(features=constants.RICH_TEXT_FEATURES, **kwargs)

    @staticmethod
    def mock(content):
        """
        Mock a TextBlock

        :param content: Format HTML
        :return: Stream content
        """
        return {"type": "text", "value": str.strip(content)}
