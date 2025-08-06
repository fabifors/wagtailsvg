from django.urls import path
from wagtail.admin.viewsets.model import ModelViewSet
from wagtailsvg.views import SvgChooserViewSet

# Create the ViewSet instance
svg_chooser_viewset = SvgChooserViewSet("svg_chooser", url_prefix="svg-chooser")

# Get the URL patterns from the ViewSet
urlpatterns = svg_chooser_viewset.get_urlpatterns()
