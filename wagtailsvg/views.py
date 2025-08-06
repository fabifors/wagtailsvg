from wagtailsvg.models import Svg
from django.utils.translation import gettext_lazy as _
from wagtail.admin.views.generic import CreateView, EditView, DeleteView
from wagtail.admin.viewsets.model import ModelViewSet


class SvgChooserViewSet(ModelViewSet):
    model = Svg
    icon = "image"
    index_template_name = "wagtailsvg/chooser/index.html"
    edit_template_name = "wagtailsvg/chooser/edit.html"
    create_template_name = "wagtailsvg/chooser/create.html"
    index_url_name = "svg_chooser:index"
    edit_url_name = "svg_chooser:edit"
    create_url_name = "svg_chooser:create"
    delete_url_name = "svg_chooser:delete"
    edit_view_class = EditView
    create_view_class = CreateView
    delete_view_class = DeleteView
    permission_policy = None
