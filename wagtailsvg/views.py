from wagtailsvg.models import Svg
from django.utils.translation import gettext_lazy as _
from wagtail.admin.views.generic import CreateView, EditView, DeleteView
from wagtail.admin.viewsets.model import ModelViewSet


class SvgChooserViewSet(ModelViewSet):
    model = Svg
    icon = "image"
    index_template_name = "modeladmin/wagtailsvg/svg/index.html"
    edit_template_name = "modeladmin/wagtailsvg/svg/edit.html"
    create_template_name = "modeladmin/wagtailsvg/svg/create.html"
    index_url_name = "wagtailsvg:index"
    edit_url_name = "wagtailsvg:edit"
    create_url_name = "wagtailsvg:create"
    delete_url_name = "wagtailsvg:delete"
    edit_view_class = EditView
    create_view_class = CreateView
    delete_view_class = DeleteView
    permission_policy = None
