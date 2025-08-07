from wagtailsvg.models import Svg
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from wagtail.admin.views.generic import CreateView, EditView, DeleteView
from wagtail.admin.viewsets.model import ModelViewSet
from wagtail.admin.viewsets.chooser import ChooserViewSet


class SvgEditView(EditView):
    """Custom edit view with preview functionality."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object and self.object.file:
            context["svg_url"] = self.object.file.url
            context["svg_filename"] = self.object.filename
        return context


class SvgModelViewSet(ModelViewSet):
    """Admin interface for managing SVGs"""

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


class SvgChooserViewSet(ChooserViewSet):
    """Chooser interface for selecting SVGs in forms/blocks"""

    model = Svg
    icon = "doc-empty-inverse"
    choose_one_text = _("Choose an SVG")
    choose_another_text = _("Change SVG")
    edit_item_text = _("Edit this SVG")
    page_title = _("Choose an SVG")

    # Use standard Wagtail chooser templates instead of custom ones
    # The standard templates handle the JavaScript communication properly

    def get_object_list(self):
        """Return the list of SVG objects for the chooser."""
        return self.model.objects.all().order_by("title")
