***********
Wagtail SVG
***********

**MODIFIED VERSION FOR WAGTAIL 6 COMPATIBILITY**

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


Setup
#####

Install with pip :

``pip install wagtailsvg``

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

Development env
###############

**If first run**

::

    git clone git@github.com:Aleksi44/wagtailsvg.git
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py init


**Run Django Server**

::

    python manage.py runserver 0.0.0.0:4243


**Run Webpack Server**

::

    yarn
    yarn start


Snoweb SVG
##########

To integrate SVG icons on Wagtail, I created Snoweb SVG with +2000 optimized SVG.
Check the `SVG library <https://github.com/Aleksi44/snoweb-svg>`_.

Feel free to contact me at `hello@snoweb.io`.

Made with ❤ by `Snoweb <https://www.snoweb.io/fr/>`_.
