from wagtailsvg.models import Svg
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from wagtail.admin.views.generic import CreateView, EditView, DeleteView
from wagtail.admin.viewsets.model import ModelViewSet


class SvgEditView(EditView):
    """Custom edit view with preview functionality."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object and self.object.file:
            context["svg_url"] = self.object.file.url
            context["svg_filename"] = self.object.filename
        return context


class SvgChooserViewSet(ModelViewSet):
    model = Svg
    icon = "image"
    index_template_name = "wagtailsvg/svg/index.html"
    edit_template_name = "wagtailsvg/svg/edit.html"
    create_template_name = "wagtailsvg/svg/create.html"
    index_url_name = "wagtailsvg:index"
    edit_url_name = "wagtailsvg:edit"
    create_url_name = "wagtailsvg:create"
    delete_url_name = "wagtailsvg:delete"
    edit_view_class = SvgEditView
    create_view_class = CreateView
    delete_view_class = DeleteView
    permission_policy = None
