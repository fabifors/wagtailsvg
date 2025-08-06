from wagtail import hooks
from wagtail.admin.site_summary import SummaryItem
from wagtailsvg.models import Svg


class SvgSummaryItem(SummaryItem):
    order = 290
    template_name = "wagtailsvg/homepage/site_summary_svg.html"

    def get_context_data(self, parent_context):
        return {
            "total_svg": Svg.objects.count(),
        }


@hooks.register("construct_homepage_summary_items")
def add_svg_summary_item(request, items):
    items.append(SvgSummaryItem(request))


@hooks.register("register_admin_viewset")
def register_svg_chooser_viewset():
    from wagtailsvg.views import SvgChooserViewSet

    return SvgChooserViewSet("wagtailsvg", url_prefix="svg")


# Register SVG as a snippet
@hooks.register("register_snippet")
def register_svg_snippet():
    return Svg
