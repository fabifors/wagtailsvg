***********
Wagtail SVG
***********

**Wagtail 6 Compatible Version**

This is a modified version of the original wagtailsvg package, adapted for Wagtail 6 compatibility.
The original work is by Alexis Le Baron. This modified version maintains the same GPL-3.0 license.

Original repository: https://github.com/Aleksi44/wagtailsvg

.. image:: https://img.shields.io/pypi/v/wagtailsvg
    :target: https://pypi.org/project/wagtailsvg/

.. image:: https://img.shields.io/pypi/pyversions/wagtailsvg
    :target: https://pypi.org/project/wagtailsvg/

`Wagtail <https://github.com/wagtail/wagtail>`_ + `SVG <https://developer.mozilla.org/docs/Web/SVG>`_ = 🚀

**SVG** for **Wagtail 6** with :

- **Svg** : Model (registered as snippet)
- **SvgChooserPanel** : Panel for ForeignKey
- **SvgChooserBlock** : ChooserBlock for StreamField

Can be used like this :

.. code-block:: python

    from wagtailsvg.models import Svg
    from wagtailsvg.blocks import SvgChooserBlock
    from wagtailsvg.edit_handlers import SvgChooserPanel


    class TestPage(Page):
        logo = models.ForeignKey(
            Svg,
            related_name='+',
            null=True,
            blank=True,
            on_delete=models.SET_NULL
        )
        body = StreamField([
            ('svg', SvgChooserBlock()),
        ], blank=True)

        content_panels = Page.content_panels + [
            SvgChooserPanel('logo'),
            FieldPanel('body'),
        ]


Installation
###########

Install from Git repository:

.. code-block:: bash

    pip install git+https://github.com/YOUR_USERNAME/wagtailsvg.git

Or add to your requirements.txt:

.. code-block:: text

    git+https://github.com/YOUR_USERNAME/wagtailsvg.git

Replace `YOUR_USERNAME` with your actual GitHub username and repository name.

Setup
#####

Add these to django apps installed :

.. code-block:: python

    INSTALLED_APPS = [
        'wagtailsvg',
        'taggit',
        ...
    ]

Set the SVG download folder in the Django settings

.. code-block:: python

    WAGTAILSVG_UPLOAD_FOLDER = 'svg'

Default value is 'media'

Requirements
###########

- Wagtail >= 6.0
- Django >= 4.2
- django-taggit

Testing
#######

Run the compatibility tests:

.. code-block:: bash

    python run_tests.py

Or run specific tests:

.. code-block:: bash

    python tests/test_wagtail6_compatibility.py

Development
##########

Clone the repository:

.. code-block:: bash

    git clone https://github.com/YOUR_USERNAME/wagtailsvg.git
    cd wagtailsvg
    pip install -r requirements.txt
    python run_tests.py

License
#######

This project is licensed under the GNU General Public License v3.0.

Original work by Alexis Le Baron.
Modified for Wagtail 6 compatibility - 2025.
